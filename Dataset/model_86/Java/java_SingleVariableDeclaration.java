





import java.util.List;
import java.util.ArrayList;

public class java_SingleVariableDeclaration extends VariableDeclaration {

    private boolean varargs;





    private java_TypeAccess java_typeaccess;




    private java_AbstractMethodDeclaration java_abstractmethoddeclaration;




    private List<java_Annotation> java_annotations;




    private java_AbstractMethodDeclaration java_abstractmethoddeclaration;


    public java_SingleVariableDeclaration(
        boolean varargs    ) {
        super(
        );
        this.varargs = varargs;
        this.java_annotations = new ArrayList<>();
    }

    public java_SingleVariableDeclaration(
        boolean varargs        ArrayList<java_Annotation> java_annotations    ) {
        this.varargs = varargs;
        this.java_annotations = java_annotations;
    }

    public boolean getVarargs() {
        return varargs;
    }

    public void setVarargs(boolean varargs) {
        this.varargs = varargs;
    }

    public java_TypeAccess getJava_typeaccess() {
        return java_typeaccess;
    }

    public void setJava_typeaccess(java_TypeAccess java_typeaccess) {
        this.java_typeaccess = java_typeaccess;
    }
    public java_AbstractMethodDeclaration getJava_abstractmethoddeclaration() {
        return java_abstractmethoddeclaration;
    }

    public void setJava_abstractmethoddeclaration(java_AbstractMethodDeclaration java_abstractmethoddeclaration) {
        this.java_abstractmethoddeclaration = java_abstractmethoddeclaration;
    }
    public List<java_Annotation> getJava_annotations() {
        return java_annotations;
    }

    public void addJava_annotation(Java_annotation java_annotation) {
        this.java_annotations.add(java_annotation);
    }
    public java_AbstractMethodDeclaration getJava_abstractmethoddeclaration() {
        return java_abstractmethoddeclaration;
    }

    public void setJava_abstractmethoddeclaration(java_AbstractMethodDeclaration java_abstractmethoddeclaration) {
        this.java_abstractmethoddeclaration = java_abstractmethoddeclaration;
    }

}