





import java.util.List;
import java.util.ArrayList;

public class java_Type extends NamedElement {






    private java_InstanceSpecification java_instancespecification;




    private List<java_InstanceSpecification> java_instancespecifications;




    private java_TypeAccess java_typeaccess;




    private List<java_TypeAccess> java_typeaccesss;


    public java_Type(
    ) {
        super(
        );
        this.java_instancespecifications = new ArrayList<>();
        this.java_typeaccesss = new ArrayList<>();
    }

    public java_Type(
        ArrayList<java_InstanceSpecification> java_instancespecifications,        ArrayList<java_TypeAccess> java_typeaccesss    ) {
        this.java_instancespecifications = java_instancespecifications;
        this.java_typeaccesss = java_typeaccesss;
    }


    public java_InstanceSpecification getJava_instancespecification() {
        return java_instancespecification;
    }

    public void setJava_instancespecification(java_InstanceSpecification java_instancespecification) {
        this.java_instancespecification = java_instancespecification;
    }
    public List<java_InstanceSpecification> getJava_instancespecifications() {
        return java_instancespecifications;
    }

    public void addJava_instancespecification(Java_instancespecification java_instancespecification) {
        this.java_instancespecifications.add(java_instancespecification);
    }
    public java_TypeAccess getJava_typeaccess() {
        return java_typeaccess;
    }

    public void setJava_typeaccess(java_TypeAccess java_typeaccess) {
        this.java_typeaccess = java_typeaccess;
    }
    public List<java_TypeAccess> getJava_typeaccesss() {
        return java_typeaccesss;
    }

    public void addJava_typeaccess(Java_typeaccess java_typeaccess) {
        this.java_typeaccesss.add(java_typeaccess);
    }

}