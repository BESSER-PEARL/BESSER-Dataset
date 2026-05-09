





import java.util.List;
import java.util.ArrayList;

public class javaDsl_ExtendsInterfaces  {

    private String interfaces;
    private String keyword;





    private javaDsl_InterfaceDeclaration javadsl_interfacedeclaration;


    public javaDsl_ExtendsInterfaces(
        String interfaces,        String keyword    ) {
        this.interfaces = interfaces;
        this.keyword = keyword;
    }


    public String getInterfaces() {
        return interfaces;
    }

    public void setInterfaces(String interfaces) {
        this.interfaces = interfaces;
    }
    public String getKeyword() {
        return keyword;
    }

    public void setKeyword(String keyword) {
        this.keyword = keyword;
    }

    public javaDsl_InterfaceDeclaration getJavadsl_interfacedeclaration() {
        return javadsl_interfacedeclaration;
    }

    public void setJavadsl_interfacedeclaration(javaDsl_InterfaceDeclaration javadsl_interfacedeclaration) {
        this.javadsl_interfacedeclaration = javadsl_interfacedeclaration;
    }

}