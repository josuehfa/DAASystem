/*
 * Copyright (c) 2015-2017 United States Government as represented by
 * the National Aeronautics and Space Administration.  No copyright
 * is claimed in the United States under Title 17, U.S.Code. All Other
 * Rights Reserved.
 */
#ifndef ALERTTHRESHOLDS_H_
#define ALERTTHRESHOLDS_H_

#include "Detection3D.h"
#include "CDCylinder.h"
#include "Vect3.h"
#include "Velocity.h"
#include "Interval.h"
#include "TrafficState.h"
#include "BandsRegion.h"
#include "ParameterData.h"
#include "ParameterTable.h"
#include <map>

namespace larcfm {

class AlertThresholds : public ParameterTable {

private:
  Detection3D* detector_; // State-based detector
  double  alerting_time_; // Alerting_time
  // If alerting_time > 0, alert is based on detection
  // If alerting_time = 0, alert is based on violation
  double early_alerting_time_; // Early alerting time (for maneuver guidance). If zero, same as alerting_time
  BandsRegion::Region region_;  // Guidance region for this alert
  double spread_trk_; // Alert when track band within spread (non-negative value)
  double spread_gs_;  // Alert when ground speed band within spread (non-negative value)
  double spread_vs_;  // Alert when vertical speed band within speed (non-negative value)
  double spread_alt_; // Alert when altitude  band within spread (non-negative value)
  std::map<std::string,std::string> units_;

public:

  static const AlertThresholds INVALID;

  bool isValid() const;

  AlertThresholds();

  /**
   * Creates an alert threholds object. Parameter det is a detector,
   * alerting_time is a non-negative alerting time (possibly positive infinity),
   * early_alerting_time is a early alerting time >= at (for maneuver guidance),
   * region is the type of guidance
   */
  AlertThresholds(const Detection3D* det,
      double alerting_time, double early_alerting_time,
      BandsRegion::Region region);

  AlertThresholds(const AlertThresholds& athr);

  ~AlertThresholds();

  // needed because of pointer
  AlertThresholds& operator=(const AlertThresholds& athr);

  /**
   * Return detector.
   */
  Detection3D* getDetectorRef() const;

  /**
   * Set detector.
   */
  void setDetector(const Detection3D* det);

  /**
   * Return alerting time in seconds.
   */
  double getAlertingTime() const;

  /**
   * Return alerting time in specified units.
   */
  double getAlertingTime(const std::string& u) const;

  /**
   * Set alerting time in seconds. Alerting time is non-negative number.
   */
  void setAlertingTime(double val);

  /**
   * Set alerting time in specified units. Alerting time is non-negative number.
   */
  void setAlertingTime(double val, const std::string& u);

  /**
   * Return early alerting time in seconds.
   */
  double getEarlyAlertingTime() const;

  /**
   * Return early alerting time in specified units.
   */
  double getEarlyAlertingTime(const std::string& u) const;

  /**
   * Set early alerting time in seconds. Early alerting time is a positive number >= alerting time
   */
  void setEarlyAlertingTime(double val);

  /**
   * Set early alerting time in specified units. Early alerting time is a positive number >= alerting time
   */
  void setEarlyAlertingTime(double val, const std::string& u);

  /**
   * Return guidance region.
   */
  BandsRegion::Region getRegion() const;

  /**
   * Set guidance region.
   */
  void setRegion(BandsRegion::Region region);

  /**
   * Get track spread in internal units [rad]. Spread is relative to ownship's track
   */
  double getTrackSpread() const;

  /**
   * Get track spread in given units [u]. Spread is relative to ownship's track
   */
  double getTrackSpread(const std::string& u) const;

  /**
   * Set track spread in internal units. Spread is relative to ownship's track and is expected
   * to be in [0,pi].
   */
  void setTrackSpread(double spread);

  /**
   * Set track spread in given units. Spread is relative to ownship's track and is expected
   * to be in [0,pi] [u].
   */
  void setTrackSpread(double spread, const std::string& u);

  /**
   * Get ground speed spread in internal units [m/s]. Spread is relative to ownship's ground speed
   */
  double getGroundSpeedSpread() const;

  /**
   * Get ground speed spread in given units. Spread is relative to ownship's ground speed
   */
  double getGroundSpeedSpread(const std::string& u) const;

  /**
   * Set ground speed spread in internal units [m/s]. Spread is relative to ownship's ground speed and is expected
   * to be non-negative
   */
  void setGroundSpeedSpread(double spread);

  /**
   * Set ground speed spread in given units. Spread is relative to ownship's ground speed and is expected
   * to be non-negative
   */
  void setGroundSpeedSpread(double spread, const std::string& u);

  /**
   * Get vertical speed spread in internal units [m/s]. Spread is relative to ownship's vertical speed
   */
  double getVerticalSpeedSpread() const;

  /**
   * Get vertical speed spread in given units. Spread is relative to ownship's vertical speed
   */
  double getVerticalSpeedSpread(const std::string& u) const;

  /**
   * Set vertical speed spread in internal units [m/s]. Spread is relative to ownship's vertical speed and is expected
   * to be non-negative
   */
  void setVerticalSpeedSpread(double spread);

  /**
   * Set vertical speed spread in given units. Spread is relative to ownship's vertical speed and is expected
   * to be non-negative
   */
  void setVerticalSpeedSpread(double spread, const std::string& u);

  /**
   * Get altitude spread in internal units [m]. Spread is relative to ownship's altitude
   */
  double getAltitudeSpread() const;

  /**
   * Get altitude spread in given units. Spread is relative to ownship's altitude
   */
  double getAltitudeSpread(const std::string& u) const;

  /**
   * Set altitude spread in internal units [m]. Spread is relative to ownship's altitude and is expected
   * to be non-negative
   */
  void setAltitudeSpread(double spread);

  /**
   * Set altitude spread in given units. Spread is relative to ownship's altitude and is expected
   * to be non-negative
   */
  void setAltitudeSpread(double spread, const std::string& u);

  std::string toString() const;

  std::string toPVS(int prec) const;

  ParameterData getParameters() const;

  void updateParameterData(ParameterData& p) const;

  void setParameters(const ParameterData& p);

  std::string getUnits(const std::string& key) const;

};
}
#endif
