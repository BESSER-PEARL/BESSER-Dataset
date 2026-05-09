





import java.util.List;
import java.util.ArrayList;

public class Java_ClassFile extends NamedElement {

    private String originalFilePath;





    private Java_Archive java_archive;




    private Java_Package java_package;




    private Java_AbstractTypeDeclaration java_abstracttypedeclaration;


    public Java_ClassFile(
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

    public Java_Archive getJava_archive() {
        return java_archive;
    }

    public void setJava_archive(Java_Archive java_archive) {
        this.java_archive = java_archive;
    }
    public Java_Package getJava_package() {
        return java_package;
    }

    public void setJava_package(Java_Package java_package) {
        this.java_package = java_package;
    }
    public Java_AbstractTypeDeclaration getJava_abstracttypedeclaration() {
        return java_abstracttypedeclaration;
    }

    public void setJava_abstracttypedeclaration(Java_AbstractTypeDeclaration java_abstracttypedeclaration) {
        this.java_abstracttypedeclaration = java_abstracttypedeclaration;
    }

}