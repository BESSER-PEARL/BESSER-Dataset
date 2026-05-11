





import java.util.List;
import java.util.ArrayList;

public class java_GenericBinding  {

    private String name;





    private java_Classifier java_classifier;




    private List<java_Classifier> java_classifiers;




    private java_Classifier java_classifier;




    private java_Classifier java_classifier;


    public java_GenericBinding(
        String name    ) {
        this.name = name;
        this.java_classifiers = new ArrayList<>();
    }

    public java_GenericBinding(
        String name        ArrayList<java_Classifier> java_classifiers    ) {
        this.name = name;
        this.java_classifiers = java_classifiers;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public java_Classifier getJava_classifier() {
        return java_classifier;
    }

    public void setJava_classifier(java_Classifier java_classifier) {
        this.java_classifier = java_classifier;
    }
    public List<java_Classifier> getJava_classifiers() {
        return java_classifiers;
    }

    public void addJava_classifier(Java_classifier java_classifier) {
        this.java_classifiers.add(java_classifier);
    }
    public java_Classifier getJava_classifier() {
        return java_classifier;
    }

    public void setJava_classifier(java_Classifier java_classifier) {
        this.java_classifier = java_classifier;
    }
    public java_Classifier getJava_classifier() {
        return java_classifier;
    }

    public void setJava_classifier(java_Classifier java_classifier) {
        this.java_classifier = java_classifier;
    }

}