





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ExtensionAttributeValue  {

    private String value;





    private bpmn2_BaseElement bpmn2_baseelement;




    private bpmn2_DocumentRoot bpmn2_documentroot;


    public bpmn2_ExtensionAttributeValue(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public bpmn2_BaseElement getBpmn2_baseelement() {
        return bpmn2_baseelement;
    }

    public void setBpmn2_baseelement(bpmn2_BaseElement bpmn2_baseelement) {
        this.bpmn2_baseelement = bpmn2_baseelement;
    }
    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }

}