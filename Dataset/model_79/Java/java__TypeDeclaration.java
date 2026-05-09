





import java.util.List;
import java.util.ArrayList;

public class java__TypeDeclaration extends AbstractTypeDeclaration {






    private List<java__TypeParameter> java__typeparameters;


    public java__TypeDeclaration(
    ) {
        super(
        );
        this.java__typeparameters = new ArrayList<>();
    }

    public java__TypeDeclaration(
        ArrayList<java__TypeParameter> java__typeparameters    ) {
        this.java__typeparameters = java__typeparameters;
    }


    public List<java__TypeParameter> getJava__typeparameters() {
        return java__typeparameters;
    }

    public void addJava__typeparameter(Java__typeparameter java__typeparameter) {
        this.java__typeparameters.add(java__typeparameter);
    }

}