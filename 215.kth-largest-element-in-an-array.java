import java.util.Comparator;
import java.util.PriorityQueue;

/*
 * @lc app=leetcode id=215 lang=java
 *
 * [215] Kth Largest Element in an Array
 *
 * https://leetcode.com/problems/kth-largest-element-in-an-array/description/
 *
 * algorithms
 * Medium (45.76%)
 * Total Accepted:    320.4K
 * Total Submissions: 700.1K
 * Testcase Example:  '[3,2,1,5,6,4]\n2'
 *
 * Find the kth largest element in an unsorted array. Note that it is the kth
 * largest element in the sorted order, not the kth distinct element.
 * 
 * Example 1:
 * 
 * 
 * Input: [3,2,1,5,6,4] and k = 2
 * Output: 5
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: [3,2,3,1,2,4,5,5,6] and k = 4
 * Output: 4
 * 
 * Note: 
 * You may assume k is always valid, 1 ≤ k ≤ array's length.
 * 
 */
class Solution {
    
    public int findKthLargest1(int[] nums, int k) {
        PriorityQueue<Integer> Q = new PriorityQueue(new Comparator<Integer>() {
            public int compare(Integer a, Integer b){
                return b-a;
            }
        });

        for(int ele : nums){
            Q.add(ele);
        }

        for(int i=0 ; i<k-1;i++){
            Q.poll();
        }
        return Q.poll();



    }

    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> Q = new PriorityQueue();
        
        for(int ele : nums){
            if (Q.size()<k){
                Q.add(ele);
            }
            else{
                if(Q.peek()<ele){
                    Q.poll();
                    Q.add(ele);
                }
            }
                  
        }
        return Q.poll();
        
    }
}
