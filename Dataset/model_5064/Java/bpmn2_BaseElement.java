





import java.util.List;
import java.util.ArrayList;

public class bpmn2_BaseElement  {

    private String name;
    private String id;
    private String anyAttribute;
    private String description;





    private bpmn2_DocumentRoot bpmn2_documentroot;




    private bpmn2_DocumentRoot bpmn2_documentroot;




    private bpmn2_Association bpmn2_association;




    private bpmn2_Association bpmn2_association;


    public bpmn2_BaseElement(
        String name,        String id,        String anyAttribute,        String description    ) {
        this.name = name;
        this.id = id;
        this.anyAttribute = anyAttribute;
        this.description = description;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }
    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }
    public bpmn2_Association getBpmn2_association() {
        return bpmn2_association;
    }

    public void setBpmn2_association(bpmn2_Association bpmn2_association) {
        this.bpmn2_association = bpmn2_association;
    }
    public bpmn2_Association getBpmn2_association() {
        return bpmn2_association;
    }

    public void setBpmn2_association(bpmn2_Association bpmn2_association) {
        this.bpmn2_association = bpmn2_association;
    }

}