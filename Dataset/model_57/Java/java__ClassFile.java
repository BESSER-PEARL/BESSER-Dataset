





import java.util.List;
import java.util.ArrayList;

public class java__ClassFile extends NamedElement {

    private String originalFilePath;





    private java__Package java__package;




    private java__AbstractTypeDeclaration java__abstracttypedeclaration;




    private java__Model java__model;




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

    public java__Package getJava__package() {
        return java__package;
    }

    public void setJava__package(java__Package java__package) {
        this.java__package = java__package;
    }
    public java__AbstractTypeDeclaration getJava__abstracttypedeclaration() {
        return java__abstracttypedeclaration;
    }

    public void setJava__abstracttypedeclaration(java__AbstractTypeDeclaration java__abstracttypedeclaration) {
        this.java__abstracttypedeclaration = java__abstracttypedeclaration;
    }
    public java__Model getJava__model() {
        return java__model;
    }

    public void setJava__model(java__Model java__model) {
        this.java__model = java__model;
    }
    public java__Archive getJava__archive() {
        return java__archive;
    }

    public void setJava__archive(java__Archive java__archive) {
        this.java__archive = java__archive;
    }

}