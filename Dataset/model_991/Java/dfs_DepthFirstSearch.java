





import java.util.List;
import java.util.ArrayList;

public class dfs_DepthFirstSearch extends EdgeProcessor {

    private int postTraversalCounter;
    private int preTraversalCounter;



    public dfs_DepthFirstSearch(
        int postTraversalCounter,        int preTraversalCounter    ) {
        super(
        );
        this.postTraversalCounter = postTraversalCounter;
        this.preTraversalCounter = preTraversalCounter;
    }


    public int getPosttraversalcounter() {
        return postTraversalCounter;
    }

    public void setPosttraversalcounter(int postTraversalCounter) {
        this.postTraversalCounter = postTraversalCounter;
    }
    public int getPretraversalcounter() {
        return preTraversalCounter;
    }

    public void setPretraversalcounter(int preTraversalCounter) {
        this.preTraversalCounter = preTraversalCounter;
    }


}