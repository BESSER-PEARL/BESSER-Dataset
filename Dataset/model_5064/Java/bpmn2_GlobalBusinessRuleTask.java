





import java.util.List;
import java.util.ArrayList;

public class bpmn2_GlobalBusinessRuleTask extends GlobalTask {

    private String implementation;





    private bpmn2_DocumentRoot bpmn2_documentroot;


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

    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }

}