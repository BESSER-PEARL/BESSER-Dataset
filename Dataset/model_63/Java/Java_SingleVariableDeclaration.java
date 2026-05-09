





import java.util.List;
import java.util.ArrayList;

public class Java_SingleVariableDeclaration extends VariableDeclaration {

    private boolean varargs;





    private List<Java_Annotation> java_annotations;




    private Java_AbstractMethodDeclaration java_abstractmethoddeclaration;




    private Java_AbstractMethodDeclaration java_abstractmethoddeclaration;




    private Java_Modifier java_modifier;




    private Java_Modifier java_modifier;




    private Java_TypeAccess java_typeaccess;


    public Java_SingleVariableDeclaration(
        boolean varargs    ) {
        super(
        );
        this.varargs = varargs;
        this.java_annotations = new ArrayList<>();
    }

    public Java_SingleVariableDeclaration(
        boolean varargs        ArrayList<Java_Annotation> java_annotations    ) {
        this.varargs = varargs;
        this.java_annotations = java_annotations;
    }

    public boolean getVarargs() {
        return varargs;
    }

    public void setVarargs(boolean varargs) {
        this.varargs = varargs;
    }

    public List<Java_Annotation> getJava_annotations() {
        return java_annotations;
    }

    public void addJava_annotation(Java_annotation java_annotation) {
        this.java_annotations.add(java_annotation);
    }
    public Java_AbstractMethodDeclaration getJava_abstractmethoddeclaration() {
        return java_abstractmethoddeclaration;
    }

    public void setJava_abstractmethoddeclaration(Java_AbstractMethodDeclaration java_abstractmethoddeclaration) {
        this.java_abstractmethoddeclaration = java_abstractmethoddeclaration;
    }
    public Java_AbstractMethodDeclaration getJava_abstractmethoddeclaration() {
        return java_abstractmethoddeclaration;
    }

    public void setJava_abstractmethoddeclaration(Java_AbstractMethodDeclaration java_abstractmethoddeclaration) {
        this.java_abstractmethoddeclaration = java_abstractmethoddeclaration;
    }
    public Java_Modifier getJava_modifier() {
        return java_modifier;
    }

    public void setJava_modifier(Java_Modifier java_modifier) {
        this.java_modifier = java_modifier;
    }
    public Java_Modifier getJava_modifier() {
        return java_modifier;
    }

    public void setJava_modifier(Java_Modifier java_modifier) {
        this.java_modifier = java_modifier;
    }
    public Java_TypeAccess getJava_typeaccess() {
        return java_typeaccess;
    }

    public void setJava_typeaccess(Java_TypeAccess java_typeaccess) {
        this.java_typeaccess = java_typeaccess;
    }

}