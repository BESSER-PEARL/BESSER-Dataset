





import java.util.List;
import java.util.ArrayList;

public class dfs_Node  {

    private int postTraversal;
    private int preTraversal;



    public dfs_Node(
        int postTraversal,        int preTraversal    ) {
        this.postTraversal = postTraversal;
        this.preTraversal = preTraversal;
    }


    public int getPosttraversal() {
        return postTraversal;
    }

    public void setPosttraversal(int postTraversal) {
        this.postTraversal = postTraversal;
    }
    public int getPretraversal() {
        return preTraversal;
    }

    public void setPretraversal(int preTraversal) {
        this.preTraversal = preTraversal;
    }


}