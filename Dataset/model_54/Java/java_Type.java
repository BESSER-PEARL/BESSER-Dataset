





import java.util.List;
import java.util.ArrayList;

public class java_Type extends NamedElement {






    private java_TypeAccess java_typeaccess;




    private java_Model java_model;




    private List<java_TypeAccess> java_typeaccesss;


    public java_Type(
    ) {
        super(
        );
        this.java_typeaccesss = new ArrayList<>();
    }

    public java_Type(
        ArrayList<java_TypeAccess> java_typeaccesss    ) {
        this.java_typeaccesss = java_typeaccesss;
    }


    public java_TypeAccess getJava_typeaccess() {
        return java_typeaccess;
    }

    public void setJava_typeaccess(java_TypeAccess java_typeaccess) {
        this.java_typeaccess = java_typeaccess;
    }
    public java_Model getJava_model() {
        return java_model;
    }

    public void setJava_model(java_Model java_model) {
        this.java_model = java_model;
    }
    public List<java_TypeAccess> getJava_typeaccesss() {
        return java_typeaccesss;
    }

    public void addJava_typeaccess(Java_typeaccess java_typeaccess) {
        this.java_typeaccesss.add(java_typeaccess);
    }

}