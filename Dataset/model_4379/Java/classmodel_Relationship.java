





import java.util.List;
import java.util.ArrayList;

public class classmodel_Relationship extends Element {

    private String label;





    private classmodel_Entity classmodel_entity;




    private classmodel_Entity classmodel_entity;


    public classmodel_Relationship(
        String label    ) {
        super(
        );
        this.label = label;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public classmodel_Entity getClassmodel_entity() {
        return classmodel_entity;
    }

    public void setClassmodel_entity(classmodel_Entity classmodel_entity) {
        this.classmodel_entity = classmodel_entity;
    }
    public classmodel_Entity getClassmodel_entity() {
        return classmodel_entity;
    }

    public void setClassmodel_entity(classmodel_Entity classmodel_entity) {
        this.classmodel_entity = classmodel_entity;
    }

}