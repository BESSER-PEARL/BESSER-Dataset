





import java.util.List;
import java.util.ArrayList;

public class JAVA_AbstractTypeDeclaration extends BodyDeclaration, Type {






    private JAVA_Package java_package;




    private List<JAVA_TypeAccess> java_typeaccesss;


    public JAVA_AbstractTypeDeclaration(
    ) {
        super(
        );
        this.java_typeaccesss = new ArrayList<>();
    }

    public JAVA_AbstractTypeDeclaration(
        ArrayList<JAVA_TypeAccess> java_typeaccesss    ) {
        this.java_typeaccesss = java_typeaccesss;
    }


    public JAVA_Package getJava_package() {
        return java_package;
    }

    public void setJava_package(JAVA_Package java_package) {
        this.java_package = java_package;
    }
    public List<JAVA_TypeAccess> getJava_typeaccesss() {
        return java_typeaccesss;
    }

    public void addJava_typeaccess(Java_typeaccess java_typeaccess) {
        this.java_typeaccesss.add(java_typeaccess);
    }

}