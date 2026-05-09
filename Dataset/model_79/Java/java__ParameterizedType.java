





import java.util.List;
import java.util.ArrayList;

public class java__ParameterizedType extends Type {






    private List<java__TypeAccess> java__typeaccesss;




    private java__TypeAccess java__typeaccess;


    public java__ParameterizedType(
    ) {
        super(
        );
        this.java__typeaccesss = new ArrayList<>();
    }

    public java__ParameterizedType(
        ArrayList<java__TypeAccess> java__typeaccesss    ) {
        this.java__typeaccesss = java__typeaccesss;
    }


    public List<java__TypeAccess> getJava__typeaccesss() {
        return java__typeaccesss;
    }

    public void addJava__typeaccess(Java__typeaccess java__typeaccess) {
        this.java__typeaccesss.add(java__typeaccess);
    }
    public java__TypeAccess getJava__typeaccess() {
        return java__typeaccess;
    }

    public void setJava__typeaccess(java__TypeAccess java__typeaccess) {
        this.java__typeaccess = java__typeaccess;
    }

}