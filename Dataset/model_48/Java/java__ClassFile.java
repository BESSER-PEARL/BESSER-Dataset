





import java.util.List;
import java.util.ArrayList;

public class java__ClassFile extends NamedElement {

    private String originalFilePath;





    private java__AbstractTypeDeclaration java__abstracttypedeclaration;




    private java__Archive java__archive;


    public java__ClassFile(
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

    public java__AbstractTypeDeclaration getJava__abstracttypedeclaration() {
        return java__abstracttypedeclaration;
    }

    public void setJava__abstracttypedeclaration(java__AbstractTypeDeclaration java__abstracttypedeclaration) {
        this.java__abstracttypedeclaration = java__abstracttypedeclaration;
    }
    public java__Archive getJava__archive() {
        return java__archive;
    }

    public void setJava__archive(java__Archive java__archive) {
        this.java__archive = java__archive;
    }

}