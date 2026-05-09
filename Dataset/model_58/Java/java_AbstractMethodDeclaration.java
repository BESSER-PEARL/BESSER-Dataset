





import java.util.List;
import java.util.ArrayList;

public class java_AbstractMethodDeclaration extends BodyDeclaration {






    private List<java_TypeAccess> java_typeaccesss;




    private List<java_SingleVariableDeclaration> java_singlevariabledeclarations;




    private java_SingleVariableDeclaration java_singlevariabledeclaration;




    private java_Block java_block;


    public java_AbstractMethodDeclaration(
    ) {
        super(
        );
        this.java_typeaccesss = new ArrayList<>();
        this.java_singlevariabledeclarations = new ArrayList<>();
    }

    public java_AbstractMethodDeclaration(
        ArrayList<java_TypeAccess> java_typeaccesss,        ArrayList<java_SingleVariableDeclaration> java_singlevariabledeclarations    ) {
        this.java_typeaccesss = java_typeaccesss;
        this.java_singlevariabledeclarations = java_singlevariabledeclarations;
    }


    public List<java_TypeAccess> getJava_typeaccesss() {
        return java_typeaccesss;
    }

    public void addJava_typeaccess(Java_typeaccess java_typeaccess) {
        this.java_typeaccesss.add(java_typeaccess);
    }
    public List<java_SingleVariableDeclaration> getJava_singlevariabledeclarations() {
        return java_singlevariabledeclarations;
    }

    public void addJava_singlevariabledeclaration(Java_singlevariabledeclaration java_singlevariabledeclaration) {
        this.java_singlevariabledeclarations.add(java_singlevariabledeclaration);
    }
    public java_SingleVariableDeclaration getJava_singlevariabledeclaration() {
        return java_singlevariabledeclaration;
    }

    public void setJava_singlevariabledeclaration(java_SingleVariableDeclaration java_singlevariabledeclaration) {
        this.java_singlevariabledeclaration = java_singlevariabledeclaration;
    }
    public java_Block getJava_block() {
        return java_block;
    }

    public void setJava_block(java_Block java_block) {
        this.java_block = java_block;
    }

}