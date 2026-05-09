





import java.util.List;
import java.util.ArrayList;

public class java_TypeDeclaration extends AbstractTypeDeclaration {






    private List<java_TypeParameter> java_typeparameters;


    public java_TypeDeclaration(
    ) {
        super(
        );
        this.java_typeparameters = new ArrayList<>();
    }

    public java_TypeDeclaration(
        ArrayList<java_TypeParameter> java_typeparameters    ) {
        this.java_typeparameters = java_typeparameters;
    }


    public List<java_TypeParameter> getJava_typeparameters() {
        return java_typeparameters;
    }

    public void addJava_typeparameter(Java_typeparameter java_typeparameter) {
        this.java_typeparameters.add(java_typeparameter);
    }

}