





import java.util.List;
import java.util.ArrayList;

public class java_Method extends Annotable, Contained {

    private boolean isFinal;
    private boolean isAbstract;
    private String name;
    private String concurrency;
    private boolean isStatic;
    private boolean isDefault;





    private List<java_Classifier> java_classifiers;




    private java_Classifier java_classifier;




    private java_Classifier java_classifier;




    private java_Classifier java_classifier;


    public java_Method(
        boolean isFinal,        boolean isAbstract,        String name,        String concurrency,        boolean isStatic,        boolean isDefault    ) {
        super(
        );
        this.isFinal = isFinal;
        this.isAbstract = isAbstract;
        this.name = name;
        this.concurrency = concurrency;
        this.isStatic = isStatic;
        this.isDefault = isDefault;
        this.java_classifiers = new ArrayList<>();
    }

    public java_Method(
        boolean isFinal,        boolean isAbstract,        String name,        String concurrency,        boolean isStatic,        boolean isDefault        ArrayList<java_Classifier> java_classifiers    ) {
        this.isFinal = isFinal;
        this.isAbstract = isAbstract;
        this.name = name;
        this.concurrency = concurrency;
        this.isStatic = isStatic;
        this.isDefault = isDefault;
        this.java_classifiers = java_classifiers;
    }

    public boolean getIsfinal() {
        return isFinal;
    }

    public void setIsfinal(boolean isFinal) {
        this.isFinal = isFinal;
    }
    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getConcurrency() {
        return concurrency;
    }

    public void setConcurrency(String concurrency) {
        this.concurrency = concurrency;
    }
    public boolean getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(boolean isStatic) {
        this.isStatic = isStatic;
    }
    public boolean getIsdefault() {
        return isDefault;
    }

    public void setIsdefault(boolean isDefault) {
        this.isDefault = isDefault;
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
    public java_Classifier getJava_classifier() {
        return java_classifier;
    }

    public void setJava_classifier(java_Classifier java_classifier) {
        this.java_classifier = java_classifier;
    }

}