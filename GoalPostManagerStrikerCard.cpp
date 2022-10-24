/**
 * @file GoalPostManagerCard.cpp
 *
 * This file implements a stiker behaviour when the ball is near the door.
 *
 * @author Elisa Santini
 */

#include "Representations/BehaviorControl/FieldBall.h"
#include "Representations/BehaviorControl/Skills.h"
#include "Representations/Configuration/FieldDimensions.h"
#include "Representations/Modeling/RobotPose.h"
#include "Tools/BehaviorControl/Framework/Card/Card.h"
#include "Tools/BehaviorControl/Framework/Card/CabslCard.h"
#include "Representations/BehaviorControl/Libraries/LibStriker.h"
#include "Representations/BehaviorControl/Libraries/LibObstacles.h"
#include "Tools/Math/BHMath.h"
#include "Representations/BehaviorControl/Libraries/LibMisc.h"
#include "Representations/Modeling/BallModel.h"

CARD(GoalPostManagerStrikerCard,
{,
  CALLS(Activity),
  CALLS(GoToBallAndKick),
  CALLS(GoToBallAndDribble),
  CALLS(LookForward),
  CALLS(Stand),
  CALLS(WalkAtRelativeSpeed),
  CALLS(WalkToPoint),
  CALLS(WalkToPose),
  CALLS(LookAtGlobalBall),
  CALLS(TurnToPoint),
  CALLS(Dribble),
  REQUIRES(FieldBall),
  REQUIRES(FieldDimensions),
  REQUIRES(RobotPose),
  REQUIRES(LibStriker),
  REQUIRES(LibObstacles),
  REQUIRES(LibMisc),
  REQUIRES(BallModel),
  DEFINES_PARAMETERS(
  {,
    (float)(0.8f) walkSpeed,
    (int)(1000) initialWaitTime,
    (int)(7000) ballNotSeenTimeout,
  }),
});

class GoalPostManagerStrikerCard : public GoalPostManagerStrikerCardBase
{
  bool preconditions() const override
  {
  //se la palla è vicina a uno dei due pali
  
    if (abs(theFieldBall.recentBallPositionOnField().x() - theFieldDimensions.xPosOpponentGoalPost) < 500.f)
    	return true;
    return false;
    
  }

  bool postconditions() const override
  {
  //se la palla non è più vicina a uno dei due pali
    
    if (abs(theFieldBall.recentBallPositionOnField().x() - theFieldDimensions.xPosOpponentGoalPost) >= 500.f)
    	return true;
    return false;
  }

  option
  {
    theActivitySkill(BehaviorStatus::Striker);

    initial_state(start)
    {
      transition
      {
        if(state_time > initialWaitTime)
          goto goToBallAndDribble;
          
      }

      action
      {
        theLookForwardSkill();
        theStandSkill();
      }
    }
    
 
    
    state(goToBallAndDribble)
    {
      transition
      {
        if(!theFieldBall.ballWasSeen(ballNotSeenTimeout))
          goto searchForBall;
          
       
        //se la palla è molto vicina a uno dei due pali e il giocatore è dalla parte sbagliata del campo
        if(((abs(theFieldBall.recentBallPositionOnField().y() - theFieldDimensions.yPosLeftGoal) < 400.f && theRobotPose.translation.y() < theFieldBall.recentBallPositionOnField().y()) || (abs(theFieldBall.recentBallPositionOnField().y() - theFieldDimensions.yPosRightGoal + 100.f) < 400.f && theRobotPose.translation.y() > theFieldBall.recentBallPositionOnField().y())) && (theFieldBall.recentBallPositionOnField().y() > theFieldDimensions.yPosLeftGoal || theFieldBall.recentBallPositionOnField().y() < (theFieldDimensions.yPosRightGoal - 100.f)))
        	goto passOverBall;
        	
        	
        //se la palla è interna alla porta
        if(theFieldBall.recentBallPositionOnField().y() <= theFieldDimensions.yPosLeftGoal && theFieldBall.recentBallPositionOnField().y() >= (theFieldDimensions.yPosRightGoal - 130.f)){
        	goto goToBallAndKick;
        }
        
        
        

      }

      action
      {
        printf("mi avvicino alla palla\n");
        //parameters: target, align precisely, kick power
        theGoToBallAndDribbleSkill(calcAngleToTarget(Vector2f(theLibStriker.GoalPostTarget())), false, 0.1f);

        
      }
    }
    
    
    
    state(passOverBall)
    {
      transition
      {
        if(!theFieldBall.ballWasSeen(ballNotSeenTimeout))
          goto searchForBall;
          
       
        //se la palla non è più vicina ai pali o sono dalla parte giusta del campo
        if(!(((abs(theFieldBall.recentBallPositionOnField().y() - theFieldDimensions.yPosLeftGoal) < 400.f && theRobotPose.translation.y() < theFieldBall.recentBallPositionOnField().y()) || (abs(theFieldBall.recentBallPositionOnField().y() - theFieldDimensions.yPosRightGoal + 100.f) < 400.f && theRobotPose.translation.y() > theFieldBall.recentBallPositionOnField().y())) && (theFieldBall.recentBallPositionOnField().y() > theFieldDimensions.yPosLeftGoal || theFieldBall.recentBallPositionOnField().y() < (theFieldDimensions.yPosRightGoal - 100.f))))
        	goto goToBallAndDribble;
        
        

      }

      action
      {
        printf("scavalco la palla\n");
        theLookAtGlobalBallSkill();
        //il target è subito oltre la palla
        Pose2f target;
        if(theFieldBall.recentBallPositionOnField().y() > 0){
            target = theLibMisc.glob2Rel(theFieldBall.recentBallPositionOnField().x(), theFieldBall.recentBallPositionOnField().y() + 300.f);
            
        }else{
            target = theLibMisc.glob2Rel(theFieldBall.recentBallPositionOnField().x(), theFieldBall.recentBallPositionOnField().y() - 300.f);    
        }
        theWalkToPointSkill(target);
        
      }
    }
    
    
    
    
    state(goToBallAndKick)
    {
      transition
      {
        if(!theFieldBall.ballWasSeen(ballNotSeenTimeout))
          goto searchForBall;
          
        
        if(((abs(theFieldBall.recentBallPositionOnField().y() - theFieldDimensions.yPosLeftGoal) < 400.f && theRobotPose.translation.y() < theFieldBall.recentBallPositionOnField().y()) || (abs(theFieldBall.recentBallPositionOnField().y() - theFieldDimensions.yPosRightGoal + 100.f) < 400.f && theRobotPose.translation.y() > theFieldBall.recentBallPositionOnField().y())) && (theFieldBall.recentBallPositionOnField().y() > theFieldDimensions.yPosLeftGoal || theFieldBall.recentBallPositionOnField().y() < (theFieldDimensions.yPosRightGoal - 100.f)))
        	goto passOverBall;
        	
        	
       if(theFieldBall.recentBallPositionOnField().y() > theFieldDimensions.yPosLeftGoal || theFieldBall.recentBallPositionOnField().y() < (theFieldDimensions.yPosRightGoal - 130.f)){
        	goto goToBallAndDribble;
        }
        
        
        

      }

      action
      {
        printf("calcio\n");
        Vector2f postleft = Vector2f(theFieldDimensions.xPosOpponentGroundLine, theFieldDimensions.yPosLeftGoal);
        Vector2f postright = Vector2f(theFieldDimensions.xPosOpponentGroundLine, theFieldDimensions.yPosRightGoal);
        //se la palla è molto vicina al palo sx o dx calcia normalmente, altrimenti calcia lungo per segnare direttamente
        if((theFieldBall.recentBallPositionOnField() - postleft).norm() < 300.f){
        	
        	theGoToBallAndKickSkill(calcAngleToTarget(Vector2f(theLibStriker.GoalPostTarget())), KickInfo::walkForwardsLeft);
        	
        } else if ((theFieldBall.recentBallPositionOnField() - postright).norm() < 300.f){
        	theGoToBallAndKickSkill(calcAngleToTarget(Vector2f(theLibStriker.GoalPostTarget())), KickInfo::walkForwardsRight);
        } else {
        	theGoToBallAndKickSkill(calcAngleToTarget(Vector2f(theLibStriker.GoalPostTarget())), KickInfo::walkForwardsLeftLong);
        }
      }
   }
    
    
    
    state(searchForBall)
    {
      transition
      {
        if(theFieldBall.ballWasSeen())
          goto goToBallAndDribble;
          
      }

      action
      {
        theLookForwardSkill();
        theWalkAtRelativeSpeedSkill(Pose2f(walkSpeed, 0.f, 0.f));
      }
    }
  }


  Angle calcAngleToTarget(Vector2f target) const
  {
    return (theRobotPose.inversePose * target).angle();
  }
};

MAKE_CARD(GoalPostManagerStrikerCard);
