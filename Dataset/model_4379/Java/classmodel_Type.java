





import java.util.List;
import java.util.ArrayList;

public class classmodel_Type  {

    private String visibility;





    private classmodel_Entity classmodel_entity;




    private classmodel_Enumeration classmodel_enumeration;




    private classmodel_Classifier classmodel_classifier;




    private classmodel_Classifier classmodel_classifier;


    public classmodel_Type(
        String visibility    ) {
        this.visibility = visibility;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }

    public classmodel_Entity getClassmodel_entity() {
        return classmodel_entity;
    }

    public void setClassmodel_entity(classmodel_Entity classmodel_entity) {
        this.classmodel_entity = classmodel_entity;
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
    public classmodel_Classifier getClassmodel_classifier() {
        return classmodel_classifier;
    }

    public void setClassmodel_classifier(classmodel_Classifier classmodel_classifier) {
        this.classmodel_classifier = classmodel_classifier;
    }

}