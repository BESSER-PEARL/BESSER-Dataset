





import java.util.List;
import java.util.ArrayList;

public class metamodel_Feature  {

    private String annotation;
    private String name;
    private String mappedBy;





    private metamodel_Type metamodel_type;




    private metamodel_Entity metamodel_entity;


    public metamodel_Feature(
        String annotation,        String name,        String mappedBy    ) {
        this.annotation = annotation;
        this.name = name;
        this.mappedBy = mappedBy;
    }


    public String getAnnotation() {
        return annotation;
    }

    public void setAnnotation(String annotation) {
        this.annotation = annotation;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMappedby() {
        return mappedBy;
    }

    public void setMappedby(String mappedBy) {
        this.mappedBy = mappedBy;
    }

    public metamodel_Type getMetamodel_type() {
        return metamodel_type;
    }

    public void setMetamodel_type(metamodel_Type metamodel_type) {
        this.metamodel_type = metamodel_type;
    }
    public metamodel_Entity getMetamodel_entity() {
        return metamodel_entity;
    }

    public void setMetamodel_entity(metamodel_Entity metamodel_entity) {
        this.metamodel_entity = metamodel_entity;
    }

}