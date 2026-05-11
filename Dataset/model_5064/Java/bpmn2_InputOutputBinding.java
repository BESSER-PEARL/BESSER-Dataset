





import java.util.List;
import java.util.ArrayList;

public class bpmn2_InputOutputBinding extends BaseElement {






    private bpmn2_InputSet bpmn2_inputset;




    private bpmn2_CallableElement bpmn2_callableelement;




    private bpmn2_DocumentRoot bpmn2_documentroot;


    public bpmn2_InputOutputBinding(
    ) {
        super(
        );
    }



    public bpmn2_InputSet getBpmn2_inputset() {
        return bpmn2_inputset;
    }

    public void setBpmn2_inputset(bpmn2_InputSet bpmn2_inputset) {
        this.bpmn2_inputset = bpmn2_inputset;
    }
    public bpmn2_CallableElement getBpmn2_callableelement() {
        return bpmn2_callableelement;
    }

    public void setBpmn2_callableelement(bpmn2_CallableElement bpmn2_callableelement) {
        this.bpmn2_callableelement = bpmn2_callableelement;
    }
    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }

}