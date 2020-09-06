# -- FILE: features/example.feature
Feature: Showing off behave

  Scenario: Run a simple test
    Given we have behave installed
     When we implement 5 tests
     Then behave will test them for us!

  Scenario: 100円でペットボトルの水を買う
    Given ユーザーが 100 円を投入して
     When "ペットボトルの水"を選択すると
     Then "ペットボトルの水"が買える
     But おつりは 0 円

  Scenario: 200円でペットボトルの水を買う
    Given ユーザーが 200 円を投入して
     When "ペットボトルの水"を選択すると
     Then "ペットボトルの水"が買える
     But おつりは 100 円

  Scenario: 200円でRedBullを買う
    Given ユーザーが 200 円を投入して
     When "RedBull"を選択すると
     Then "RedBull"が買える
     But おつりは 0 円