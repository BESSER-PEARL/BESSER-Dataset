





import java.util.List;
import java.util.ArrayList;

public class java__TypeParameter extends Type {






    private List<java__TypeAccess> java__typeaccesss;


    public java__TypeParameter(
    ) {
        super(
        );
        this.java__typeaccesss = new ArrayList<>();
    }

    public java__TypeParameter(
        ArrayList<java__TypeAccess> java__typeaccesss    ) {
        this.java__typeaccesss = java__typeaccesss;
    }


    public List<java__TypeAccess> getJava__typeaccesss() {
        return java__typeaccesss;
    }

    public void addJava__typeaccess(Java__typeaccess java__typeaccess) {
        this.java__typeaccesss.add(java__typeaccess);
    }

}