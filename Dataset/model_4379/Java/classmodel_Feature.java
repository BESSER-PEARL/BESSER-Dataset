





import java.util.List;
import java.util.ArrayList;

public class classmodel_Feature  {

    private String visibility;
    private String constraint;
    private String value;
    private String name;





    private classmodel_Enumeration classmodel_enumeration;




    private classmodel_Classifier classmodel_classifier;


    public classmodel_Feature(
        String visibility,        String constraint,        String value,        String name    ) {
        this.visibility = visibility;
        this.constraint = constraint;
        this.value = value;
        this.name = name;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getConstraint() {
        return constraint;
    }

    public void setConstraint(String constraint) {
        this.constraint = constraint;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public classmodel_Enumeration getClassmodel_enumeration() {
        return classmodel_enumeration;
    }

    public void setClassmodel_enumeration(classmodel_Enumeration classmodel_enumeration) {
        this.classmodel_enumeration = classmodel_enumeration;
    }
    public classmodel_Classifier getClassmodel_classifier() {
        return classmodel_classifier;
    }

    public void setClassmodel_classifier(classmodel_Classifier classmodel_classifier) {
        this.classmodel_classifier = classmodel_classifier;
    }

}