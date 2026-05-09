





import java.util.List;
import java.util.ArrayList;

public class java_AbstractMethodDeclaration extends BodyDeclaration {






    private java_AbstractMethodInvocation java_abstractmethodinvocation;




    private List<java_AbstractMethodInvocation> java_abstractmethodinvocations;




    private List<java_MethodRef> java_methodrefs;




    private java_MethodRef java_methodref;


    public java_AbstractMethodDeclaration(
    ) {
        super(
        );
        this.java_abstractmethodinvocations = new ArrayList<>();
        this.java_methodrefs = new ArrayList<>();
    }

    public java_AbstractMethodDeclaration(
        ArrayList<java_AbstractMethodInvocation> java_abstractmethodinvocations,        ArrayList<java_MethodRef> java_methodrefs    ) {
        this.java_abstractmethodinvocations = java_abstractmethodinvocations;
        this.java_methodrefs = java_methodrefs;
    }


    public java_AbstractMethodInvocation getJava_abstractmethodinvocation() {
        return java_abstractmethodinvocation;
    }

    public void setJava_abstractmethodinvocation(java_AbstractMethodInvocation java_abstractmethodinvocation) {
        this.java_abstractmethodinvocation = java_abstractmethodinvocation;
    }
    public List<java_AbstractMethodInvocation> getJava_abstractmethodinvocations() {
        return java_abstractmethodinvocations;
    }

    public void addJava_abstractmethodinvocation(Java_abstractmethodinvocation java_abstractmethodinvocation) {
        this.java_abstractmethodinvocations.add(java_abstractmethodinvocation);
    }
    public List<java_MethodRef> getJava_methodrefs() {
        return java_methodrefs;
    }

    public void addJava_methodref(Java_methodref java_methodref) {
        this.java_methodrefs.add(java_methodref);
    }
    public java_MethodRef getJava_methodref() {
        return java_methodref;
    }

    public void setJava_methodref(java_MethodRef java_methodref) {
        this.java_methodref = java_methodref;
    }

}