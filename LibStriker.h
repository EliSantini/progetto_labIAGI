/**
 * @file LibStriker.h
 *
 * This file defines a representation that holds some utilities (primarily) for the striker.
 *
 * @author Francesco Petri
 */

#pragma once

#include "Tools/Function.h"
#include "Tools/Math/Eigen.h"
#include "Tools/Streams/AutoStreamable.h"
#include "Representations/Modeling/FreeGoalTargetableArea.h"

STREAMABLE(LibStriker,
{
  /** 
   * @author Emanuele Musumeci
   * Returns the global y coord point we are looking at on the opponent groundline
   */
  FUNCTION(float()) projectGazeOntoOpponentGroundline;

  /**
   * @author Emanuele Antonioni
   * 
   * Gives the best movement point for the striker selecting it between five fixed point (center, right, left, very right, very left)
   * */
  FUNCTION(Vector2f()) strikerMovementPoint;

  /** Provides a vector with the point of beginning and finish of goal areas free from opponent coverage
   * @param myPose pose of the robot
   * @param opponents the opponent vector (global coordinates)
   * @return vector of free areas
   */
  FUNCTION(std::vector<FreeGoalTargetableArea>(float minimumDiscretizedAreaSize)) computeFreeAreas;
  
  /** Provides the best point to shoot at inside the goal.
   * If the opponent goal is completely occluded returns the field center (exactly (0,0))
   * @param shootASAP If set to true, if the robot is near the goal, shoot in the spot nearest to where you're looking at ("As Soon As Possible"), else use the heuristic to decide
   * @param forceHeuristic If set to true, always use the heuristic to decide where to shoot
   * @return the Vector2f of the position selected to shoot
   * **/
  FUNCTION(Vector2f(bool shootASAP, bool forceHeuristic)) goalTarget;
  
  /** Variant of goalTarget that also return the FreeGoalTargetableArea associated to the target point.
    * @param shootASAP If set to true has the robot will shoot to the nearest accessible point, located inside the nearest targetable area
    * @param forceHeuristic If set to true, always use the heuristic to decide where to shoot
    * @return the Vector2f of the position selected to shoot
    * **/
  FUNCTION(std::pair<Vector2f, FreeGoalTargetableArea>(bool shootASAP, bool forceHeuristic)) goalTargetWithArea;

  /**
   * Groups some conditions common to a couple striker cards.
   * TODO this is likely to end up unused, check after porting.
   *      The cards in question are unlikely to be ported to the new [2023] repo.
   */
  FUNCTION(bool(int hysteresisSign)) strikerPassCommonConditions;
  
  
  FUNCTION(bool(const Vector2f& point, float radius)) areThereOpponentsNearTarget;
  
  /**
   * Provides the target for the striker when the ball is near the goal post
   */
  FUNCTION(Vector2f()) GoalPostTarget,
});
