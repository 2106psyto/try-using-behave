Feature: 品物が買える

  Scenario Outline: KennyVendorで品物を買う
    Given ユーザーが <charge> 円を投入して
     When <item>を選択すると
     Then <item>が買えて
     But おつりは<change>円

  Examples: 飲み物
    |charge|item|change|
    |100|"ペットボトルの水"|0|
    |200|"ペットボトルの水"|100|
    |200|"RedBull"|0|

  Examples: 食べ物
    |charge|item|change|
    |500|"おでん"|0|
    |1000|"おでん"|500|
