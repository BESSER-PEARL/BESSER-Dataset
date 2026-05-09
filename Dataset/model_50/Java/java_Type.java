





import java.util.List;
import java.util.ArrayList;

public class java_Type extends NamedElement {






    private List<java_TypeAccess> java_typeaccesss;




    private java_TypeAccess java_typeaccess;


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


    public List<java_TypeAccess> getJava_typeaccesss() {
        return java_typeaccesss;
    }

    public void addJava_typeaccess(Java_typeaccess java_typeaccess) {
        this.java_typeaccesss.add(java_typeaccess);
    }
    public java_TypeAccess getJava_typeaccess() {
        return java_typeaccess;
    }

    public void setJava_typeaccess(java_TypeAccess java_typeaccess) {
        this.java_typeaccess = java_typeaccess;
    }

}