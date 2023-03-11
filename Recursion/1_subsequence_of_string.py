
# https://www.codingninjas.com/codestudio/problems/subsequences-of-string_985087?leftPanelTab=0&utm_source=youtube&utm_medium=affiliate&utm_campaign=love_babbar_16



def helper(str, i, output, ans):

    if i==len(str):
        if len(output)!=0:
            l1=output.copy()
            ans.append("".join(l1))
        return

    output.append(str[i])
    helper(str, i+1,output, ans)

    output.pop()
    helper(str, i + 1, output, ans)


def subsequences(str):
    ans=[]
    output=[]
    helper(str, 0, output, ans)
    return ans

print(subsequence("abc"))

