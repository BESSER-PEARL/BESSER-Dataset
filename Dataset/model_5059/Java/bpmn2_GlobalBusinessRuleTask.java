





import java.util.List;
import java.util.ArrayList;

public class bpmn2_GlobalBusinessRuleTask extends GlobalTask {

    private String implementation;



    public bpmn2_GlobalBusinessRuleTask(
        String implementation    ) {
        super(
        );
        this.implementation = implementation;
    }


    public String getImplementation() {
        return implementation;
    }

    public void setImplementation(String implementation) {
        this.implementation = implementation;
    }


}