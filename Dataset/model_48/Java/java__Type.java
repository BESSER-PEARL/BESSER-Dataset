





import java.util.List;
import java.util.ArrayList;

public class java__Type extends NamedElement {






    private java__TypeAccess java__typeaccess;




    private List<java__TypeAccess> java__typeaccesss;


    public java__Type(
    ) {
        super(
        );
        this.java__typeaccesss = new ArrayList<>();
    }

    public java__Type(
        ArrayList<java__TypeAccess> java__typeaccesss    ) {
        this.java__typeaccesss = java__typeaccesss;
    }


    public java__TypeAccess getJava__typeaccess() {
        return java__typeaccess;
    }

    public void setJava__typeaccess(java__TypeAccess java__typeaccess) {
        this.java__typeaccess = java__typeaccess;
    }
    public List<java__TypeAccess> getJava__typeaccesss() {
        return java__typeaccesss;
    }

    public void addJava__typeaccess(Java__typeaccess java__typeaccess) {
        this.java__typeaccesss.add(java__typeaccess);
    }

}