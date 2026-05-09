





import java.util.List;
import java.util.ArrayList;

public class java__AnonymousClassDeclaration extends ASTNode {






    private java__EnumConstantDeclaration java__enumconstantdeclaration;




    private java__ClassInstanceCreation java__classinstancecreation;




    private List<java__BodyDeclaration> java__bodydeclarations;




    private java__ClassInstanceCreation java__classinstancecreation;




    private java__BodyDeclaration java__bodydeclaration;


    public java__AnonymousClassDeclaration(
    ) {
        super(
        );
        this.java__bodydeclarations = new ArrayList<>();
    }

    public java__AnonymousClassDeclaration(
        ArrayList<java__BodyDeclaration> java__bodydeclarations    ) {
        this.java__bodydeclarations = java__bodydeclarations;
    }


    public java__EnumConstantDeclaration getJava__enumconstantdeclaration() {
        return java__enumconstantdeclaration;
    }

    public void setJava__enumconstantdeclaration(java__EnumConstantDeclaration java__enumconstantdeclaration) {
        this.java__enumconstantdeclaration = java__enumconstantdeclaration;
    }
    public java__ClassInstanceCreation getJava__classinstancecreation() {
        return java__classinstancecreation;
    }

    public void setJava__classinstancecreation(java__ClassInstanceCreation java__classinstancecreation) {
        this.java__classinstancecreation = java__classinstancecreation;
    }
    public List<java__BodyDeclaration> getJava__bodydeclarations() {
        return java__bodydeclarations;
    }

    public void addJava__bodydeclaration(Java__bodydeclaration java__bodydeclaration) {
        this.java__bodydeclarations.add(java__bodydeclaration);
    }
    public java__ClassInstanceCreation getJava__classinstancecreation() {
        return java__classinstancecreation;
    }

    public void setJava__classinstancecreation(java__ClassInstanceCreation java__classinstancecreation) {
        this.java__classinstancecreation = java__classinstancecreation;
    }
    public java__BodyDeclaration getJava__bodydeclaration() {
        return java__bodydeclaration;
    }

    public void setJava__bodydeclaration(java__BodyDeclaration java__bodydeclaration) {
        this.java__bodydeclaration = java__bodydeclaration;
    }

}