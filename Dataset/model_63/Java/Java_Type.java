





import java.util.List;
import java.util.ArrayList;

public class Java_Type extends NamedElement {






    private Java_TypeAccess java_typeaccess;




    private List<Java_TypeAccess> java_typeaccesss;


    public Java_Type(
    ) {
        super(
        );
        this.java_typeaccesss = new ArrayList<>();
    }

    public Java_Type(
        ArrayList<Java_TypeAccess> java_typeaccesss    ) {
        this.java_typeaccesss = java_typeaccesss;
    }


    public Java_TypeAccess getJava_typeaccess() {
        return java_typeaccess;
    }

    public void setJava_typeaccess(Java_TypeAccess java_typeaccess) {
        this.java_typeaccess = java_typeaccess;
    }
    public List<Java_TypeAccess> getJava_typeaccesss() {
        return java_typeaccesss;
    }

    public void addJava_typeaccess(Java_typeaccess java_typeaccess) {
        this.java_typeaccesss.add(java_typeaccess);
    }

}