





import java.util.List;
import java.util.ArrayList;

public class java_AbstractMethodDeclaration extends BodyDeclaration {






    private java_AbstractMethodInvocation java_abstractmethodinvocation;




    private java_Block java_block;




    private List<java_TypeAccess> java_typeaccesss;


    public java_AbstractMethodDeclaration(
    ) {
        super(
        );
        this.java_typeaccesss = new ArrayList<>();
    }

    public java_AbstractMethodDeclaration(
        ArrayList<java_TypeAccess> java_typeaccesss    ) {
        this.java_typeaccesss = java_typeaccesss;
    }


    public java_AbstractMethodInvocation getJava_abstractmethodinvocation() {
        return java_abstractmethodinvocation;
    }

    public void setJava_abstractmethodinvocation(java_AbstractMethodInvocation java_abstractmethodinvocation) {
        this.java_abstractmethodinvocation = java_abstractmethodinvocation;
    }
    public java_Block getJava_block() {
        return java_block;
    }

    public void setJava_block(java_Block java_block) {
        this.java_block = java_block;
    }
    public List<java_TypeAccess> getJava_typeaccesss() {
        return java_typeaccesss;
    }

    public void addJava_typeaccess(Java_typeaccess java_typeaccess) {
        this.java_typeaccesss.add(java_typeaccess);
    }

}