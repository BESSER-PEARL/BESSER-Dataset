





import java.util.List;
import java.util.ArrayList;

public class metamodel_HibernateAnnotation  {

    private String unique;
    private String cascade;
    private String annotationType;





    private metamodel_Attribute metamodel_attribute;




    private metamodel_Attribute metamodel_attribute;


    public metamodel_HibernateAnnotation(
        String unique,        String cascade,        String annotationType    ) {
        this.unique = unique;
        this.cascade = cascade;
        this.annotationType = annotationType;
    }


    public String getUnique() {
        return unique;
    }

    public void setUnique(String unique) {
        this.unique = unique;
    }
    public String getCascade() {
        return cascade;
    }

    public void setCascade(String cascade) {
        this.cascade = cascade;
    }
    public String getAnnotationtype() {
        return annotationType;
    }

    public void setAnnotationtype(String annotationType) {
        this.annotationType = annotationType;
    }

    public metamodel_Attribute getMetamodel_attribute() {
        return metamodel_attribute;
    }

    public void setMetamodel_attribute(metamodel_Attribute metamodel_attribute) {
        this.metamodel_attribute = metamodel_attribute;
    }
    public metamodel_Attribute getMetamodel_attribute() {
        return metamodel_attribute;
    }

    public void setMetamodel_attribute(metamodel_Attribute metamodel_attribute) {
        this.metamodel_attribute = metamodel_attribute;
    }

}