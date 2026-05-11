





import java.util.List;
import java.util.ArrayList;

public class java_Argument  {

    private int order;
    private String name;





    private java_Method java_method;




    private java_Classifier java_classifier;




    private java_Method java_method;


    public java_Argument(
        int order,        String name    ) {
        this.order = order;
        this.name = name;
    }


    public int getOrder() {
        return order;
    }

    public void setOrder(int order) {
        this.order = order;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public java_Method getJava_method() {
        return java_method;
    }

    public void setJava_method(java_Method java_method) {
        this.java_method = java_method;
    }
    public java_Classifier getJava_classifier() {
        return java_classifier;
    }

    public void setJava_classifier(java_Classifier java_classifier) {
        this.java_classifier = java_classifier;
    }
    public java_Method getJava_method() {
        return java_method;
    }

    public void setJava_method(java_Method java_method) {
        this.java_method = java_method;
    }

}