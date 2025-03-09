// Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
// Basically, the deletion can be divided into two stages:
// Search for a node to remove.
// If the node is found, delete the node.


public class DeleteNodeInABST {
    public void deleteNode(TreeNode root, int key) {


        if (root == null) return root;


        if (root.val > key) {
            root.left = deleteNode(root.left, key);
        }
        else if (root.val < key) {
            root.right = deleteNode(root.right, key);
        }
        else {
            // No children
            if (root.left == null && root.right == null) {
                //return null;
            }

            
            else if (root.right == null) {
                return root.left;
            }
            else if (root.left == null) {
                return root.right;
            }
            else {
                return root.left;
            }


        }

        
    }






           
}
