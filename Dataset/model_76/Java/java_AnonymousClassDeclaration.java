





import java.util.List;
import java.util.ArrayList;

public class java_AnonymousClassDeclaration extends ASTNode {






    private List<java_BodyDeclaration> java_bodydeclarations;




    private java_ClassInstanceCreation java_classinstancecreation;




    private java_ClassInstanceCreation java_classinstancecreation;




    private java_BodyDeclaration java_bodydeclaration;


    public java_AnonymousClassDeclaration(
    ) {
        super(
        );
        this.java_bodydeclarations = new ArrayList<>();
    }

    public java_AnonymousClassDeclaration(
        ArrayList<java_BodyDeclaration> java_bodydeclarations    ) {
        this.java_bodydeclarations = java_bodydeclarations;
    }


    public List<java_BodyDeclaration> getJava_bodydeclarations() {
        return java_bodydeclarations;
    }

    public void addJava_bodydeclaration(Java_bodydeclaration java_bodydeclaration) {
        this.java_bodydeclarations.add(java_bodydeclaration);
    }
    public java_ClassInstanceCreation getJava_classinstancecreation() {
        return java_classinstancecreation;
    }

    public void setJava_classinstancecreation(java_ClassInstanceCreation java_classinstancecreation) {
        this.java_classinstancecreation = java_classinstancecreation;
    }
    public java_ClassInstanceCreation getJava_classinstancecreation() {
        return java_classinstancecreation;
    }

    public void setJava_classinstancecreation(java_ClassInstanceCreation java_classinstancecreation) {
        this.java_classinstancecreation = java_classinstancecreation;
    }
    public java_BodyDeclaration getJava_bodydeclaration() {
        return java_bodydeclaration;
    }

    public void setJava_bodydeclaration(java_BodyDeclaration java_bodydeclaration) {
        this.java_bodydeclaration = java_bodydeclaration;
    }

}