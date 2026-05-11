





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Extension  {

    private boolean mustUnderstand;
    private String xsdDefinition;





    private bpmn2_DocumentRoot bpmn2_documentroot;




    private bpmn2_Definitions bpmn2_definitions;


    public bpmn2_Extension(
        boolean mustUnderstand,        String xsdDefinition    ) {
        this.mustUnderstand = mustUnderstand;
        this.xsdDefinition = xsdDefinition;
    }


    public boolean getMustunderstand() {
        return mustUnderstand;
    }

    public void setMustunderstand(boolean mustUnderstand) {
        this.mustUnderstand = mustUnderstand;
    }
    public String getXsddefinition() {
        return xsdDefinition;
    }

    public void setXsddefinition(String xsdDefinition) {
        this.xsdDefinition = xsdDefinition;
    }

    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }
    public bpmn2_Definitions getBpmn2_definitions() {
        return bpmn2_definitions;
    }

    public void setBpmn2_definitions(bpmn2_Definitions bpmn2_definitions) {
        this.bpmn2_definitions = bpmn2_definitions;
    }

}