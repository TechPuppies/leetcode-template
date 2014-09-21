// AC Rate: 22.9%
// https://oj.leetcode.com/problems/clone-graph/

// Clone an undirected graph. Each node in the graph contains a label and a list
// OJ's undirected graph serialization:
// Nodes are labeled uniquely.
// We use # as a separator for each node, and , as a separator for node label and
// As an example, consider the serialized graph {0,1,2#1,2#2,2}.
// The graph has a total of three nodes, and therefore contains three parts as
// First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
// Second node is labeled as 1. Connect node 1 to node 2.
// Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a
// Visually, the graph looks like the following:
//        1
//       / \
//      /   \
//     0 --- 2
//          / \
//          \_/

import java.util.*;

/**
 * Definition for undirected graph.
 * class UndirectedGraphNode {
 *     int label;
 *     List<UndirectedGraphNode> neighbors;
 *     UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
 * };
 */
public class Solution {
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        
    }
}