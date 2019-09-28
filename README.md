# XL Release License Usage Plugin

[![Build Status][xlr-license-usage-plugin-travis-image]][xlr-license-usage-plugin-travis-url]
[![Codacy Badge][xlr-license-usage-plugin-codacy-image] ][xlr-license-usage-plugin-codacy-url]
[![Code Climate][xlr-license-usage-plugin-code-climate-image] ][xlr-license-usage-plugin-code-climate-url]
[![License: MIT][xlr-license-usage-plugin-license-image]][xlr-license-usage-plugin-license-url]
[![Github All Releases][xlr-license-usage-plugin-downloads-image]]()

## Preface

This document describes the functionality provided by the XL Release xlr-license-usage-plugin. 

See the [XL Release reference manual](https://docs.xebialabs.com/xl-release) for background information on XL Release and release automation concepts.  

## Overview

The plugin makes available two global tiles to display license useage.  One for XL Release and one for XL Deploy.  You can create a custom global dashboard and add these tiles to it.

## Requirements

* **Requirements**
*  **XL Release**   9.0.0+

## Installation

* Copy the latest JAR file from the [releases page](https://github.com/xebialabs-community/xlr-license-usage-plugin/releases) into the `XL_RELEASE_SERVER/plugins/__local__` directory.
* Restart the XL Release server.

## Usage

**Steps**

1. Navigate to Dashboards tab
1. Click 'Add New Dashboard' button
    1. Select 'blank' dashboard template
    1. Give your new dashboard a name and description
1. Click 'Configure Dashboard' button
1. Click 'Add Tile" button
1. Select 'License : XL Release' tile
1. Optionally select 'License : XL Deploy' tile
    1. Configure XL Deploy tile by selecting an XL Deploy server you've configured in Settings -> Shared Configuration

## Developers

Build and package the plugins with...

```bash
./gradlew assemble
```

[xlr-license-usage-plugin-travis-image]: https://travis-ci.org/xebialabs-community/xlr-license-usage-plugin.svg?branch=master
[xlr-license-usage-plugin-travis-url]: https://travis-ci.org/xebialabs-community/xlr-license-usage-plugin

[xlr-license-usage-plugin-codacy-image]: https://api.codacy.com/project/badge/Grade/88dec34743b84dac8f9aaaa665a99207
[xlr-license-usage-plugin-codacy-url]: https://www.codacy.com/app/ladamato/xlr-license-usage-plugin

[xlr-license-usage-plugin-code-climate-image]: https://codeclimate.com/github/xebialabs-community/xlr-license-usage-plugin/badges/gpa.svg
[xlr-license-usage-plugin-code-climate-url]: https://codeclimate.com/github/xebialabs-community/xlr-license-usage-plugin

[xlr-license-usage-plugin-license-image]: https://img.shields.io/badge/License-MIT-yellow.svg
[xlr-license-usage-plugin-license-url]: https://opensource.org/licenses/MIT
[xlr-license-usage-plugin-downloads-image]: https://img.shields.io/github/downloads/xebialabs-community/xlr-license-usage-plugin/total.svg
