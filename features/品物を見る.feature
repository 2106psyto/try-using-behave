Feature: 品物の一覧が調べられる
  Scenario: NishiVendorで品物の一覧を調べる
    Given ユーザーがお金を投入していないとき
     When 任意の品物を選択すると
     Then 商品の一覧が返る
