





import java.util.List;
import java.util.ArrayList;

public class java_TypeParameter extends Type {






    private java_TypeDeclaration java_typedeclaration;




    private List<java_TypeAccess> java_typeaccesss;


    public java_TypeParameter(
    ) {
        super(
        );
        this.java_typeaccesss = new ArrayList<>();
    }

    public java_TypeParameter(
        ArrayList<java_TypeAccess> java_typeaccesss    ) {
        this.java_typeaccesss = java_typeaccesss;
    }


    public java_TypeDeclaration getJava_typedeclaration() {
        return java_typedeclaration;
    }

    public void setJava_typedeclaration(java_TypeDeclaration java_typedeclaration) {
        this.java_typedeclaration = java_typedeclaration;
    }
    public List<java_TypeAccess> getJava_typeaccesss() {
        return java_typeaccesss;
    }

    public void addJava_typeaccess(Java_typeaccess java_typeaccess) {
        this.java_typeaccesss.add(java_typeaccess);
    }

}