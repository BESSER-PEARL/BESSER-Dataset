





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Resource extends RootElement {






    private bpmn2_ResourceRole bpmn2_resourcerole;




    private bpmn2_DocumentRoot bpmn2_documentroot;


    public bpmn2_Resource(
    ) {
        super(
        );
    }



    public bpmn2_ResourceRole getBpmn2_resourcerole() {
        return bpmn2_resourcerole;
    }

    public void setBpmn2_resourcerole(bpmn2_ResourceRole bpmn2_resourcerole) {
        this.bpmn2_resourcerole = bpmn2_resourcerole;
    }
    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }

}