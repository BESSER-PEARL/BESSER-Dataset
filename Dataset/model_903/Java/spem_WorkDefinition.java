





import java.util.List;
import java.util.ArrayList;

public class spem_WorkDefinition  {

    private String postCondition;
    private String preCondition;





    private spem_WorkDefinitionPerformer spem_workdefinitionperformer;


    public spem_WorkDefinition(
        String postCondition,        String preCondition    ) {
        this.postCondition = postCondition;
        this.preCondition = preCondition;
    }


    public String getPostcondition() {
        return postCondition;
    }

    public void setPostcondition(String postCondition) {
        this.postCondition = postCondition;
    }
    public String getPrecondition() {
        return preCondition;
    }

    public void setPrecondition(String preCondition) {
        this.preCondition = preCondition;
    }

    public spem_WorkDefinitionPerformer getSpem_workdefinitionperformer() {
        return spem_workdefinitionperformer;
    }

    public void setSpem_workdefinitionperformer(spem_WorkDefinitionPerformer spem_workdefinitionperformer) {
        this.spem_workdefinitionperformer = spem_workdefinitionperformer;
    }

}