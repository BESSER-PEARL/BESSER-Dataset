





import java.util.List;
import java.util.ArrayList;

public class java_ClassFile extends NamedElement {

    private String originalFilePath;





    private java_Package java_package;




    private java_AbstractTypeDeclaration java_abstracttypedeclaration;


    public java_ClassFile(
        String originalFilePath    ) {
        super(
        );
        this.originalFilePath = originalFilePath;
    }


    public String getOriginalfilepath() {
        return originalFilePath;
    }

    public void setOriginalfilepath(String originalFilePath) {
        this.originalFilePath = originalFilePath;
    }

    public java_Package getJava_package() {
        return java_package;
    }

    public void setJava_package(java_Package java_package) {
        this.java_package = java_package;
    }
    public java_AbstractTypeDeclaration getJava_abstracttypedeclaration() {
        return java_abstracttypedeclaration;
    }

    public void setJava_abstracttypedeclaration(java_AbstractTypeDeclaration java_abstracttypedeclaration) {
        this.java_abstracttypedeclaration = java_abstracttypedeclaration;
    }

}