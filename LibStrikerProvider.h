/**
 * @file LibStrikerProvider.h
 * 
 * See LibStriker
 *
 * @author Francesco Petri
 */

#pragma once

#include "Representations/Modeling/RobotPose.h"
#include "Representations/Configuration/FieldDimensions.h"
#include "Representations/Modeling/OpponentGoalModel.h"
#include "Representations/Modeling/TeamPlayersModel.h"
#include "Representations/BehaviorControl/FieldBall.h"
#include "Representations/spqr_representations/PassShare.h"
#include "Representations/BehaviorControl/Libraries/LibMisc.h"
#include "Representations/BehaviorControl/Libraries/LibStriker.h"
#include "Representations/Configuration/FieldDimensions.h"
#include "Tools/Module/Module.h"
#include "Representations/BehaviorControl/Libraries/LibObstacles.h"


MODULE(LibStrikerProvider,
{,
  REQUIRES(RobotPose),
  REQUIRES(FieldDimensions),
  REQUIRES(TeamPlayersModel),
  REQUIRES(FieldBall),    // TODO was only for strikerPassCommonConditions
  REQUIRES(PassShare),    // TODO was only for strikerPassCommonConditions
  REQUIRES(LibMisc),
  REQUIRES(LibObstacles),
  PROVIDES(LibStriker),
  USES(OpponentGoalModel),
  // LOADS_PARAMETERS(
  // {,
  //   // nothing for now!
  // }),
});

class LibStrikerProvider : public LibStrikerProviderBase
{
private:
  
  /**
   * Updates LibStriker
   * @param libStriker The representation provided
   */
  void update(LibStriker& libStriker) override;


  // ===== IMPLEMENTATIONS OF LibStriker =====

  /** Returns the global y coord point we are looking at on the opponent groundline*/
  float projectGazeOntoOpponentGroundline() const;

  /** Provides a vector with the point of beginning and finish of goal areas free from opponent coverage
   * @param myPose pose of the robot
   * @param opponents the opponent vector (global coordinates)
   * @return vector of free areas
   */
  std::vector<FreeGoalTargetableArea> computeFreeAreas(float minimumDiscretizedAreaSize) const;

  /** Provides the best point to shoot at inside the goal.
   * If the opponent goal is completely occluded returns the field center (exactly (0,0))
   * @param shootASAP If set to true, if the robot is near the goal, shoot in the spot nearest to where you're looking at ("As Soon As Possible"), else use the heuristic to decide
   * @param forceHeuristic If set to true, always use the heuristic to decide where to shoot
   * @return the Vector2f of the position selected to shoot
   * **/
  Vector2f goalTarget(bool shootASAP, bool forceHeuristic) const;

  /** Variant of goalTarget that also return the FreeGoalTargetableArea associated to the target point.
    * @param shootASAP If set to true has the robot will shoot to the nearest accessible point, located inside the nearest targetable area
    * @param forceHeuristic If set to true, always use the heuristic to decide where to shoot
    * @return the Vector2f of the position selected to shoot
    * **/
  std::pair<Vector2f, FreeGoalTargetableArea> goalTargetWithArea(bool shootASAP, bool forceHeuristic) const;

  /**
   * Groups some conditions common to a couple striker cards.
   * TODO this is likely to end up unused, check after porting.
   *      The cards in question are unlikely to be ported to the new [2023] repo.
   */
  bool strikerPassCommonConditions(int hysteresisSign) const;


  // ===== FOR INTERNAL USE =====

  /** @author Emanuele Musumeci
   * Given a certain point in input proivdes its projection on the opponent ground line by the robot's perspective
   * @param x x global coordinate of point to be projected
   * @param y y global coordinate of point to be projected
   * @return Global y coord of the projected point
   */
  float projectPointOntoOpponentGroundline(float x, float y) const;

  /** Tells whether two segments are overlapping or not
   * @param l1 left limit of first segment
   * @param r1 right limit of the first segment
   * @param l2 left limit of the second segment
   * @param r2 right limit of the second segment
   * @return bool value
   * **/
  bool areOverlappingSegmentsOnYAxis (float l1, float r1, float l2, float r2) const;

  /** Provides a float value representing a score for each FreeGoalTargetableArea Determined by computeFreeAreas
   * @param leftLimit left limit of the free targetable area
   * @param rightLimit right limit of the free targetable area
   * @param poles_weight relative weight in the final utility for the poles
   * @param opponents_weight relative weight in the final utility for the opponents
   * @param teammates_weight relative weight in the final utility for the teammates
   * @return value assigned after area evaluation
   * **/
  float areaValueHeuristic(float leftLimit, float rightLimit, float poles_weight = 1, float opponents_weight = 1, float teammates_weight = 1) const;

  /**
   * Returns the distance of the opponent closest to the given point, squared.
   */
  float sqrDistanceOfClosestOpponentToPoint(const Vector2f& p) const;

  /**
   * @author Emanuele Antonioni
   * 
   * Gives the best movement point for the striker selecting it between five fixed point (center, right, left, very right, very left)
   * */
  Vector2f strikerMovementPoint() const;
  
  /**
   * Provides the target for the striker when the ball is near the goal post
   */
  Vector2f GoalPostTarget() const;
  
  //returns whether there are opponents near a given point in global coordinates
  bool areThereOpponentsNearTarget(const Vector2f& point, float radius) const;
};
