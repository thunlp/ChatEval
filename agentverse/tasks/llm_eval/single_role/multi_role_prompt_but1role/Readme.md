###注意
这里的base setting指的是在summary场景下会有一个src article, 然后有一个generated text,所以本质上也是pair
comparison,但是并不是真的两段文本孰优孰劣，pair comparison还得重新再试试 感觉这个才会作为base line

现在这个multi_role_prompt_but1role指的是我没修改prompt, 保持跟multi_role一样的prompt  
不过咱需要测试不同三个role: General Public, Critic, News Author
之后写进scripts, 现在都是手动改