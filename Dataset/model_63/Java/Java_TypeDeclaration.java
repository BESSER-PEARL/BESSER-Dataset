





import java.util.List;
import java.util.ArrayList;

public class Java_TypeDeclaration extends AbstractTypeDeclaration {






    private List<Java_TypeParameter> java_typeparameters;


    public Java_TypeDeclaration(
    ) {
        super(
        );
        this.java_typeparameters = new ArrayList<>();
    }

    public Java_TypeDeclaration(
        ArrayList<Java_TypeParameter> java_typeparameters    ) {
        this.java_typeparameters = java_typeparameters;
    }


    public List<Java_TypeParameter> getJava_typeparameters() {
        return java_typeparameters;
    }

    public void addJava_typeparameter(Java_typeparameter java_typeparameter) {
        this.java_typeparameters.add(java_typeparameter);
    }

}