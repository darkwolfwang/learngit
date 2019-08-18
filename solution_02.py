# -*- coding: utf-8 -*-
#给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

#如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

'''
本题三种解法，都不正确，前两种问题小一点，结果应该是807，跑的答案是797，应该是有逻辑错了，目前找不出来，留待日后能力更强再找

'''

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

"""
解题分析，先要搞清楚listnode是啥，简单百度一下这里不解释，直接分析题目
1,链表对应结点增加时增加前一个结点的进位，并保存下一结点的进位
2，两个链表长度不一时，要处理较长的链表剩余高位和进位计算的值
3，如果最高计算时还产生进位，则需要添加一个额外的结点
"""
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        jinwei = 0
        result = []
        count = 0
        while l1!=None and l2!=None:
            sum = l1.val + l2.val + jinwei
            if sum>9:
                result.append(ListNode(sum-10))
                jinwei = 1
            else:
                result.append(ListNode(sum))
                jinwei = 0
            l1 = l1.next
            l2 = l2.next
            if count!=0:          #第一次是两个数个位相加，result列表中只有一个元素，所以不需要执行这条语句
                result[-2].next = result[-1]
            count = 1
        
        while l1!=None:
            sum = l1.val + jinwei
            if sum>9:
                result.append(ListNode(sum-10))
                jinwei = 1
            else:
                result.append(ListNode(sum))
                jinwei = 0
            l1 = l1.next
            result[-2].next = result[-1]
        
        while l2!=None:
            sum = l2.val + jinwei
            if sum>9:
                result.append(ListNode(sum-10))
                jinwei = 1
            else:
                result.append(ListNode(sum))
                jinwei = 0
            l2 = l2.next
            result[-2].next = result[-1]
        if jinwei == 1:
            result[-1].next = ListNode(jinwei)
        
        return result[0]

    def addTwoNumbers_2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        jinwei=0
        result=[]
        count=0
        while l1!=None and l2!=None:
        	sum=l1.val+l2.val+jinwei
        	if sum>9:
        		result.append(ListNode(sum-10))
        		jinwei=1
        	else:
        		result.append(ListNode(sum))
        		jinwei=0
        	l1=l1.next
        	l2=l2.next
        	if count!=0: #第一次是两个数个位相加，result列表中只有一个元素，所以不需要执行下面这条语句
        		result[-2].next=result[-1]
        	count=1

        while l1!=None:
        	sum=l1.val+jinwei
        	if sum>9:
        		result.append(ListNode(sum-10))
        		jinwei=1
        	else:
        		result.append(ListNode(sum))
        		jinwei=0
        	l1=l1.next
        	result[-2].next=result[-1]

        while l2!=None:
        	sum=l2.val+jinwei
        	if sum>9:
        		result.append(ListNode(sum-10))
        		jinwei=1
        	else:
        		result.append(ListNode(sum))
        		jinwei=0
        	l2=l2.next
        	result[-2].next=result[-1]

        if jinwei==1:
        	result[-1].next=ListNode(jinwei)
        return result[0]

    def addTwoNumbers_3(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p=result=ListNode (-1)
        temp=0
        while l1 and l2:#当l1和l2属于同长度部分
            sum=l1.val+l2.val+temp
            temp=int(sum/10)
            ptemp=ListNode(sum%10)
            p.next=ptemp
            
            p=p.next
            l1=l1.next
            l2=l2.next
            
        temp1=l1 or l2
            
        while temp1:#当l1和l2属于不同长度部分
            sum=temp1.val+temp
            temp=int(sum/10)
            ptemp=ListNode(sum%10)
            p.next=ptemp
            
            p=p.next
            temp1=temp1.next
        if temp:
            p.next=ListNode(temp)
        return result.next
s = Solution()
l1 = ListNode(243)
l2 = ListNode(564)
l3 = s.addTwoNumbers_3(l1, l2)
print(l3.val)