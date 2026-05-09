





import java.util.List;
import java.util.ArrayList;

public class Java5_TypeDeclaration extends AbstractTypeDeclaration {






    private List<Java5_TypeParameter> java5_typeparameters;


    public Java5_TypeDeclaration(
    ) {
        super(
        );
        this.java5_typeparameters = new ArrayList<>();
    }

    public Java5_TypeDeclaration(
        ArrayList<Java5_TypeParameter> java5_typeparameters    ) {
        this.java5_typeparameters = java5_typeparameters;
    }


    public List<Java5_TypeParameter> getJava5_typeparameters() {
        return java5_typeparameters;
    }

    public void addJava5_typeparameter(Java5_typeparameter java5_typeparameter) {
        this.java5_typeparameters.add(java5_typeparameter);
    }

}