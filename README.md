# hapoma(HatenaPostMan)

はてなブログ投稿用のスクリプトです．

markdownで記述したファイルを送信できます(現在は下書きのみ)．
もし一度でも投稿したことのあるファイルであれば，ブログを更新してくれます．

# 使い方
```
hapoma あいうえお.md
```

# 設定

まずはconfigファイルを編集しましょう．
configに設定なのは

- consumer_key(はてなから発行される公開鍵)
- consumer_secret(はてなから発行される秘密鍵)
- api_key(ブログの設定あたりに書いてあります)
- rootendpoint(はてなブログの投稿用のURL)
- oauth_token(はてなから発行されるワンタイムパスワード)
- oauth_token_secret(はてなから発行されるワンタイムパスワード)
- oauth_verifier(鍵をつかって取得できるPINコード)
- access_token(鍵とPINコードをつかって取得できるパスワード)
- access_token(鍵とPINコードをつかって取得できるパスワード)


# 参考
この記事を読むとconsumerキーとアクセストークン，Verifierの取得の流れが書いてあります．
[http://developer.hatena.ne.jp/ja/documents/auth/apis/oauth/consumer]
[http://developer.hatena.ne.jp/ja/documents/blog/apis/atom]
