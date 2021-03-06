# XL Release License Usage Plugin

[![Build Status][xlr-license-usage-tile-travis-image]][xlr-license-usage-tile-travis-url]
[![Codacy Badge][xlr-license-usage-tile-codacy-image] ][xlr-license-usage-tile-codacy-url]
[![Code Climate][xlr-license-usage-tile-code-climate-image] ][xlr-license-usage-tile-code-climate-url]
[![License: MIT][xlr-license-usage-tile-license-image]][xlr-license-usage-tile-license-url]
[![Github All Releases][xlr-license-usage-tile-downloads-image]]()

## Preface

This document describes the functionality provided by the XL Release xlr-license-usage-tile. 

See the [XL Release reference manual](https://docs.xebialabs.com/xl-release) for background information on XL Release and release automation concepts.  

## Overview

The plugin makes available two global tiles to display license useage.  One for XL Release and one for XL Deploy.  You can create a custom global dashboard and add these tiles to it.

## Requirements

* **Requirements**
* **XL Release**   9.0.0+

## Installation

* Copy the latest JAR file from the [releases page](https://github.com/xebialabs-community/xlr-license-usage-tile/releases) into the `XL_RELEASE_SERVER/plugins/__local__` directory.
* Restart the XL Release server.

## Usage

**Steps**

***Overall***

When viewing Dashboards note that there are two modes: Configuration Mode and View Mode. Switch between the two by clicking the buttons displayed on the right side of the screen.

### Configure Mode

![Configure](images/configureMode.png)

### View Mode

![View](images/viewMode.png)

***Create the Dashboard***

1. Navigate to Dashboards tab
1. Click 'Add New Dashboard' button
    1. Select 'blank' dashboard template
    2. Give your new dashboard a name and description
    3. Provide any permissions for this dashboard, then press 'Create'

***XL Release Usage***

1. Click 'Add Tile" button
2. Select 'License : XL Release' tile
3. If you'd like to limit the number of days since last login to consider a user inactive, press the gear icon on the tile and set your *Last Use Cutoff* value.
4. Press Save.

![AddTiles](images/addTiles.png)

***XL Deploy Usage***

1. Confirm you have a XL Deploy instance defined in XL Release (Settings|Shared Configuration|XL Deploy Server)
2. Click 'Add Tile" button
3. On your usage dashboard, Select 'License : XL Deploy' tile
   1. you can safely ignore a 500 error message, since you need to define which XL Deploy instance you will be tracking
4. Click on the gear icon, and choose your XL Deploy server
5. If needed, you can also define a different username and/or password for the XL Deploy instance you are tracking.
6. Press Save.

![ConfigureXLD](images/configure.png)

### Tiles Display

![Tiles](images/viewMode.png)

### XL Release Users Detail

While in View Mode, if you click the 'expand' icon in the upper right corner, you will see a user detail page as shown below.  XL Release doesn't have a concept of 'active' or 'inactive' users.  Instead the tile has a property 'days since login', defaulting to 30 days, that groups users as active or inactive.  Anyone who has not logged in within the last 'days since login' are considered inactive.

![XLR Users](images/xlr-Detail.png)

### XL Deploy Users Detail

While in View Mode, if you click the 'expand' icon in the upper right corner, you will see a user detail page as shown below.  Note that XL Deploy does not track last login date so the tile is unable to differentiate between active and inactive users.

![XLD Users](images/xld-Detail.png)

## Developers

Build and package the plugins with...

```bash
./gradlew assemble
```

[xlr-license-usage-tile-travis-image]: https://travis-ci.org/xebialabs-community/xlr-license-usage-tile.svg?branch=master
[xlr-license-usage-tile-travis-url]: https://travis-ci.org/xebialabs-community/xlr-license-usage-tile

[xlr-license-usage-tile-codacy-image]: https://api.codacy.com/project/badge/Grade/88dec34743b84dac8f9aaaa665a99207
[xlr-license-usage-tile-codacy-url]: https://www.codacy.com/app/ladamato/xlr-license-usage-tile

[xlr-license-usage-tile-code-climate-image]: https://codeclimate.com/github/xebialabs-community/xlr-license-usage-tile/badges/gpa.svg
[xlr-license-usage-tile-code-climate-url]: https://codeclimate.com/github/xebialabs-community/xlr-license-usage-tile

[xlr-license-usage-tile-license-image]: https://img.shields.io/badge/License-MIT-yellow.svg
[xlr-license-usage-tile-license-url]: https://opensource.org/licenses/MIT
[xlr-license-usage-tile-downloads-image]: https://img.shields.io/github/downloads/xebialabs-community/xlr-license-usage-tile/total.svg
