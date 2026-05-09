





import java.util.List;
import java.util.ArrayList;

public class Java5_AnonymousClassDeclaration extends ASTNode {






    private Java5_EnumConstantDeclaration java5_enumconstantdeclaration;




    private Java5_ClassInstanceCreation java5_classinstancecreation;




    private Java5_ClassInstanceCreation java5_classinstancecreation;




    private Java5_BodyDeclaration java5_bodydeclaration;




    private List<Java5_BodyDeclaration> java5_bodydeclarations;


    public Java5_AnonymousClassDeclaration(
    ) {
        super(
        );
        this.java5_bodydeclarations = new ArrayList<>();
    }

    public Java5_AnonymousClassDeclaration(
        ArrayList<Java5_BodyDeclaration> java5_bodydeclarations    ) {
        this.java5_bodydeclarations = java5_bodydeclarations;
    }


    public Java5_EnumConstantDeclaration getJava5_enumconstantdeclaration() {
        return java5_enumconstantdeclaration;
    }

    public void setJava5_enumconstantdeclaration(Java5_EnumConstantDeclaration java5_enumconstantdeclaration) {
        this.java5_enumconstantdeclaration = java5_enumconstantdeclaration;
    }
    public Java5_ClassInstanceCreation getJava5_classinstancecreation() {
        return java5_classinstancecreation;
    }

    public void setJava5_classinstancecreation(Java5_ClassInstanceCreation java5_classinstancecreation) {
        this.java5_classinstancecreation = java5_classinstancecreation;
    }
    public Java5_ClassInstanceCreation getJava5_classinstancecreation() {
        return java5_classinstancecreation;
    }

    public void setJava5_classinstancecreation(Java5_ClassInstanceCreation java5_classinstancecreation) {
        this.java5_classinstancecreation = java5_classinstancecreation;
    }
    public Java5_BodyDeclaration getJava5_bodydeclaration() {
        return java5_bodydeclaration;
    }

    public void setJava5_bodydeclaration(Java5_BodyDeclaration java5_bodydeclaration) {
        this.java5_bodydeclaration = java5_bodydeclaration;
    }
    public List<Java5_BodyDeclaration> getJava5_bodydeclarations() {
        return java5_bodydeclarations;
    }

    public void addJava5_bodydeclaration(Java5_bodydeclaration java5_bodydeclaration) {
        this.java5_bodydeclarations.add(java5_bodydeclaration);
    }

}