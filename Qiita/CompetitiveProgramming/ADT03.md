
- [初めに](#初めに)
- [まずはEASYに参加してみた。](#まずはeasyに参加してみた)
  - [D問題　Sandwich Number](#d問題sandwich-number)
    - [問題](#問題)
    - [解法](#解法)
    - [コード](#コード)
    - [ChatGPT先生！（1回目）](#chatgpt先生1回目)
    - [解説コード](#解説コード)
  - [E問題 Final Day](#e問題-final-day)
    - [問題](#問題-1)
    - [解法](#解法-1)
    - [コード](#コード-1)
    - [ChatGPT先生！(2回目)](#chatgpt先生2回目)
- [MEDIUMにも参加してみた。](#mediumにも参加してみた)
  - [F問題 Approximate Equalization 2](#f問題-approximate-equalization-2)
    - [問題](#問題-2)
    - [解法](#解法-2)
    - [コードその１](#コードその１)
    - [ChatGPT先生！（3回目）](#chatgpt先生3回目)
  - [ChatGPT先生、ありがとう！(n回目)](#chatgpt先生ありがとうn回目)
- [終わりに](#終わりに)

# 初めに

AtCoderさんが主催されている練習用バーチャルコンテスト、AtCoder Daily Trainingに初めて(2023年11月2日)参加してみました。ChatGPT先生の力を大いに借りたので、そのあたりの振り返りも含めて記事を書いていきます。

https://atcoder.jp/contests/adt_top/


AtCoder Daily Training (以後はADTと呼称します)はAtCoder主催の練習用バーチャルコンテストであり、1日2回、火曜、水曜、木曜の午後に開催されています。詳しくは上のページをご覧ください。

一度に開催されているADTには4種類あります。難易度順に、EASY, MEDIUM, HARD, ALLです。それぞれの対象者としては次のように記載されています。

| 難易度 | 対象者 | 問題難易度 |
|:------:|:------:|:---------:|
|EASY | 初心者、灰| AABBC|
|MEDIUM| 茶、緑 | BBCCD |
|HARD | 水、青 | CCDEF |
|ALL | 水、青 | AABBCCDEF |

とりあえず様子見でEASYに参加してみました。

# まずはEASYに参加してみた。
![image-7.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2611731/8a8f93cb-ca9f-bf9e-a11d-87c651a4b095.png)

![image-6.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2611731/e824e4bf-03f6-1f5f-3af9-ae527ff307c5.png)


全完でしたがめちゃくちゃREを出しました。REが出た問題を軽く振り返っていきます。

## D問題　Sandwich Number 

https://atcoder.jp/contests/adt_easy_20231102_1/tasks/abc281_b

### 問題
英大文字と数字からなる文字列が与えられるので、条件を満たすか判定する。

### 解法
条件を一個ずつ確かめるような愚直な解法を取りました。

1. 長さが8か確かめる
2. 一文字目が英大文字か確かめる
3. 最後の文字が英大文字か確かめる
4. 中間が全て数字か確かめる

### コード

こんなコードを最初に書きました。

```python
def main():
    S = list(input())
    flag = True 
    if len(S) != 8: flag = False
    if not S[0].isupper(): flag = False
    if not S[-1].isupper(): flag = False

    for i in range(1, 7):
        if i == 1 and int(S[i]) == 0:
            flag = False
        if not S[i].isnumeric():
            flag = False
    
    if flag:
        print("Yes")
    else:
        print("No")

main()
```
これを投げると`RE`が出てしまいました。`RE`ということはどこかでエラーが出ています。ちゃんと考えるとすぐわかるミスをしていたのですが、一旦ChatGPT先生に投げてみます。

### ChatGPT先生！（1回目）

> The code you provided appears to be checking whether a given string meets specific criteria for validation. The corner cases to consider would be input strings that test the boundaries of the validation conditions. Here are some corner cases to consider:
>
> 1. An input string with a length other than 8:
> For example, if S has fewer than 8 characters or more than 8 characters.
> 2. An input string where the first character is not an uppercase letter:
> For example, if the first character is a lowercase letter or a non-alphabetical character.
>3. An input string where the last character is not an uppercase letter: For example, if the last character is a lowercase letter or a non-alphabetical character.
>4. An input string where the second character is not a digit and the rest are numeric:
For example, if the second character is a letter or a special character, but the remaining characters are numbers.
>5. An input string where characters between the second and the second-to-last are not numeric: For example, if any character between positions 2 and 6 is not a number.
>
> These corner cases are important to consider to ensure that the code correctly validates the input string according to the specified criteria. Depending on the specific requirements and constraints, you might need to handle these cases differently.


すごい、問題すら投げていないのにちゃんと文脈で判断してくれます。コーナーケースをちゃんと言語化してくれるのが有難いです。

一つ目のコーナーケース、Sが長い/短い時のことを考えてみると、Sが8文字以外でもそのまま続行してしまっていたことに気づきました。

修正コードがこちら


```python
S = list(input())
flag = True 
if len(S) != 8: flag = False
else:
    if not S[0].isupper(): flag = False
    if not S[-1].isupper(): flag = False

    for i in range(1, 7):
        if i == 1 and int(S[i]) == 0:
            flag = False
        if not S[i].isnumeric():
            flag = False

if flag:
    print("Yes")
else:
    print("No")
```

これで`AC`が取れました。

### 解説コード

ちなみに解説コードではもっと簡潔に綺麗に書かれていたのでリンクだけ貼っておきます。

https://atcoder.jp/contests/abc281/submissions/37074572


## E問題 Final Day

https://atcoder.jp/contests/adt_easy_20231102_1/tasks/abc228_c

E問題というと仰々しいですが普通に灰diffの問題です。

### 問題
試験を4日間くらい行います。3日目までの結果を渡すので4日目でK位以内に入る可能性はあるかな？

### 解法
最終日にその人だけ満点を取りそれ以外の人が0点を取る想定で、最終的にK位に入れるか確認します。

### コード
最初は満点を300点ではなく100点と勘違いし、更に添え字を間違えて`RE`をたたき出しました。修正後のコードがこちら。

```python
def main():
    N, K = map(int, input().split())
    score_sums = []
    for _ in range(N):
        s = list(is_map(int))
        score_sums.append(sum(s))
    
    score_sums_sorted = sorted(score_sums, reverse = True)

    for i in range(N):
        final_score = score_sums[i] + 300
        if final_score >= score_sums_sorted[K-1]:
            print("Yes")
        else:
            print("No")
main()
```

### ChatGPT先生！(2回目)

またコーナーケースを考えてもらいます。

> The corner case for this code could involve the input values and the output when dealing with different values of N and K.
> 
> Here are some corner cases to consider:
> 
> 1. N and K both equal 1: 
> 
> When both N and K are 1, you can test how the code handles the smallest input values.
> 
> 2. All scores are equal:
> 
> You might want to test a case where all the scores for each player are equal to see if the code handles it correctly.
> 
> 3. Maximum possible values for N and K:
> 
> Test the code with the largest possible values of N and K to see if it performs efficiently and gives correct results.
> 
> 4. A case where no player qualifies:
> 
> For example, you can have K set to a very high value, and all players have very low scores. In this case, you want to check if the code correctly handles the situation when no player qualifies
> 
> 5. Random values for N and K:
> 
> Test the code with various random values for N and K to see how it behaves with different inputs.
> 
> 
> By testing these corner cases, you can verify if the code handles various scenarios and produces the expected results under different conditions. This helps ensure that your solution is robust and works as intended for a wide range of inputs.

問題文を教えずにコードだけ入れてコーナーケースを訊いても、前半部分は割と的を得たことを言っています。

# MEDIUMにも参加してみた。

EASYは`RE`は出したものの方針に困ることもなく完走できたので、次の回でMEDIUMにも参加してみました。

![image-8.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2611731/1c5527a0-0471-a564-10af-e88bd1cf80e2.png)

4完でした。

## F問題 Approximate Equalization 2

茶diffの問題です。

https://atcoder.jp/contests/adt_medium_20231102_2/tasks/abc313_c

### 問題
整数のリストが与えられるので、二つ要素を選んで±１する操作を繰り返しながら最大値と最小値の差を1以内にしてね。

### 解法
平均を見つけ、何回操作すれば全ての要素を平均前後に持ってこられるか計算します。

### コードその１
とりあえず書いてみました　→　`WA`!!!!!

```python

def main():
    N = int(input())
    A = list(map(int, input().split()))

    min_A = sum(A) // len(A)
    max_A = sum(A) // len(A) + 1

    move_up = 0
    move_down = 0

    for i in range(N):
        if A[i] < min_A:
            move_up += (min_A - A[i])    
        elif A[i] > max_A:
            move_down += (A[i] - A[i])
    
    if N == 1:
        return 0
    else return max(move_up, move_down)

print(main())
```
あれ～解法は合ってると思うんだけどな～？

こういう時は…？

### ChatGPT先生！（3回目）

コードを投げて、何で違うんだと思う？と聞いてみました。

> There are a few issues in your code, including a logical error and some syntax issues. Let me help you correct those and identify the potential corner cases to consider:
> 
> Here's the corrected code:
> 
> ```python
>def main():
>   N = int(input())
>   A = list(is_map(int))
>
>  min_A = sum(A) // len(A)
>   max_A = sum(A) // len(A) + 1
>
>   move_up = 0
>   move_down = 0
>   
>   for i in range(N):
>       if A[i] < min_A:
>           move_up += (min_A - A[i])
>       elif A[i] > max_A:
>           move_down += (A[i] - max_A)
>   
>   if N == 1:
>       return 0
>   else:
>       return max(move_up, move_down)
>
> print(main())
> ```

…

ほんとだ！

```move_down += (A[i] - max_A)```

この部分、`max_A`と書かなきゃいけないところがどちらも`A[i]`になってました。ChatGPT先生ありがとう！

`AC`です。


## ChatGPT先生、ありがとう！(n回目)

ChatGPT先生に大いに助けられたADTでした。ChatGPT先生を使う上で、いくつか自分なりに気を付けていることがあるのでまとめておきます。

+ 英語で質問する。
    回答の精度が英語と日本語だと全然違います。

+ 問題文をコピペするときは改行を削除してからにする。
    問題文をそのままコピーすると改行が残ってしまい読み取りの精度が悪くなります。改行はURLバーに一回貼り付けてから再度コピーしなおすことで簡単に削除できます。

+ ChatGPT先生、方針を立てるときの助けにはあまりなってくれない。

    AtCoder社長のchokudaiさんのブログから引用します。

> 競プロ以外を見た時に、チャットAIでは以下のような傾向があるように思えます。
> 
> 1. 単純に覚えれば良いもの、書き方を参照すれば良いものは答えられる
> 2. 工夫が必要なものはあまり答えられない
> 3. 単純なバグなどは自力で修正出来るが、根本的なロジックは修正出来ない

https://chokudai.hatenablog.com/entry/2022/12/07/161959

  その通りで、「この問題どうしたら解ける？」と聞いても大した答えは返ってきません。しかし、先程のようなエラーの解決などでは焦りで見えていなかった視点を提供してくれたりします。

  書き方参照としての使い方もかなり便利です。

例えば`a`から`o`までのリストを作りたかったとします。ChatGPT先生はかなりこちらの気持ちをくみ取ってくれるので、こんなシンプルなリクエストにすぐ応えてくれます。

> make a list from a to o 


> You can create a list containing letters from 'a' to 'o' using a list comprehension. Here's how you can do it:
> ```python
> letters_list = [chr(ord('a') + i) for i in range(15)]
> ```
> The `letters_list` will contain the letters from 'a' to 'o'.


優秀ですね。

+  終わったらちゃんとお礼を言います。

    人としての礼儀ってもんですよね。

> thank you for all the help. 


> You're welcome! If you have any more questions or need further assistance in the future, feel free to reach out. Good luck with your coding and any other endeavors you're pursuing! Have a great day!


# 終わりに

ADT,　11月2日分をChatGPT先生と完走した振り返り記事でした。今の自分としては、MEDIUMが滅茶苦茶苦労するわけではないけどちょっと時間かかるくらいの問題でちょうどいいので、これからも時間の限り参加していこうと思います。

ADTの運営されている方、ありがとうございます！

目標はMEDIUM時間内全完です！



