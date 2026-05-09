





import java.util.List;
import java.util.ArrayList;

public class javaMM_SingleVariableDeclaration extends VariableDeclaration {

    private String varargs;





    private javaMM_AbstractMethodDeclaration javamm_abstractmethoddeclaration;




    private javaMM_TypeAccess javamm_typeaccess;




    private List<javaMM_Annotation> javamm_annotations;




    private javaMM_AbstractMethodDeclaration javamm_abstractmethoddeclaration;


    public javaMM_SingleVariableDeclaration(
        String varargs    ) {
        super(
        );
        this.varargs = varargs;
        this.javamm_annotations = new ArrayList<>();
    }

    public javaMM_SingleVariableDeclaration(
        String varargs        ArrayList<javaMM_Annotation> javamm_annotations    ) {
        this.varargs = varargs;
        this.javamm_annotations = javamm_annotations;
    }

    public String getVarargs() {
        return varargs;
    }

    public void setVarargs(String varargs) {
        this.varargs = varargs;
    }

    public javaMM_AbstractMethodDeclaration getJavamm_abstractmethoddeclaration() {
        return javamm_abstractmethoddeclaration;
    }

    public void setJavamm_abstractmethoddeclaration(javaMM_AbstractMethodDeclaration javamm_abstractmethoddeclaration) {
        this.javamm_abstractmethoddeclaration = javamm_abstractmethoddeclaration;
    }
    public javaMM_TypeAccess getJavamm_typeaccess() {
        return javamm_typeaccess;
    }

    public void setJavamm_typeaccess(javaMM_TypeAccess javamm_typeaccess) {
        this.javamm_typeaccess = javamm_typeaccess;
    }
    public List<javaMM_Annotation> getJavamm_annotations() {
        return javamm_annotations;
    }

    public void addJavamm_annotation(Javamm_annotation javamm_annotation) {
        this.javamm_annotations.add(javamm_annotation);
    }
    public javaMM_AbstractMethodDeclaration getJavamm_abstractmethoddeclaration() {
        return javamm_abstractmethoddeclaration;
    }

    public void setJavamm_abstractmethoddeclaration(javaMM_AbstractMethodDeclaration javamm_abstractmethoddeclaration) {
        this.javamm_abstractmethoddeclaration = javamm_abstractmethoddeclaration;
    }

}