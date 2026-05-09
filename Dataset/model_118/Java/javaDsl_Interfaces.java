





import java.util.List;
import java.util.ArrayList;

public class javaDsl_Interfaces  {

    private String interfaces;
    private String keyword;





    private javaDsl_ClassDeclaration javadsl_classdeclaration;


    public javaDsl_Interfaces(
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

    public javaDsl_ClassDeclaration getJavadsl_classdeclaration() {
        return javadsl_classdeclaration;
    }

    public void setJavadsl_classdeclaration(javaDsl_ClassDeclaration javadsl_classdeclaration) {
        this.javadsl_classdeclaration = javadsl_classdeclaration;
    }

}