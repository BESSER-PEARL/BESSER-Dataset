





import java.util.List;
import java.util.ArrayList;

public class spem_WorkDefinition  {

    private String preCondition;
    private String postCondition;



    public spem_WorkDefinition(
        String preCondition,        String postCondition    ) {
        this.preCondition = preCondition;
        this.postCondition = postCondition;
    }


    public String getPrecondition() {
        return preCondition;
    }

    public void setPrecondition(String preCondition) {
        this.preCondition = preCondition;
    }
    public String getPostcondition() {
        return postCondition;
    }

    public void setPostcondition(String postCondition) {
        this.postCondition = postCondition;
    }


}