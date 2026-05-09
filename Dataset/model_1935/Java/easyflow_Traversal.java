





import java.util.List;
import java.util.ArrayList;

public class easyflow_Traversal extends ITraversal {

    private String tarversalCriterion;



    public easyflow_Traversal(
        String tarversalCriterion    ) {
        super(
        );
        this.tarversalCriterion = tarversalCriterion;
    }


    public String getTarversalcriterion() {
        return tarversalCriterion;
    }

    public void setTarversalcriterion(String tarversalCriterion) {
        this.tarversalCriterion = tarversalCriterion;
    }


}