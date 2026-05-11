





import java.util.List;
import java.util.ArrayList;

public class DecisionTree_PropertySpec2  {

    private boolean needsTypeCheck;





    private DecisionTree_IntermediateNode decisiontree_intermediatenode;


    public DecisionTree_PropertySpec2(
        boolean needsTypeCheck    ) {
        this.needsTypeCheck = needsTypeCheck;
    }


    public boolean getNeedstypecheck() {
        return needsTypeCheck;
    }

    public void setNeedstypecheck(boolean needsTypeCheck) {
        this.needsTypeCheck = needsTypeCheck;
    }

    public DecisionTree_IntermediateNode getDecisiontree_intermediatenode() {
        return decisiontree_intermediatenode;
    }

    public void setDecisiontree_intermediatenode(DecisionTree_IntermediateNode decisiontree_intermediatenode) {
        this.decisiontree_intermediatenode = decisiontree_intermediatenode;
    }

}