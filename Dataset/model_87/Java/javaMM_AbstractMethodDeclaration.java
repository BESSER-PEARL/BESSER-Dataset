





import java.util.List;
import java.util.ArrayList;

public class javaMM_AbstractMethodDeclaration extends BodyDeclaration {






    private List<javaMM_SingleVariableDeclaration> javamm_singlevariabledeclarations;




    private javaMM_AbstractMethodInvocation javamm_abstractmethodinvocation;




    private List<javaMM_TypeParameter> javamm_typeparameters;




    private List<javaMM_MethodRef> javamm_methodrefs;




    private javaMM_MethodRef javamm_methodref;




    private javaMM_SingleVariableDeclaration javamm_singlevariabledeclaration;




    private List<javaMM_AbstractMethodInvocation> javamm_abstractmethodinvocations;




    private List<javaMM_TypeAccess> javamm_typeaccesss;


    public javaMM_AbstractMethodDeclaration(
    ) {
        super(
        );
        this.javamm_singlevariabledeclarations = new ArrayList<>();
        this.javamm_typeparameters = new ArrayList<>();
        this.javamm_methodrefs = new ArrayList<>();
        this.javamm_abstractmethodinvocations = new ArrayList<>();
        this.javamm_typeaccesss = new ArrayList<>();
    }

    public javaMM_AbstractMethodDeclaration(
        ArrayList<javaMM_SingleVariableDeclaration> javamm_singlevariabledeclarations,        ArrayList<javaMM_TypeParameter> javamm_typeparameters,        ArrayList<javaMM_MethodRef> javamm_methodrefs,        ArrayList<javaMM_AbstractMethodInvocation> javamm_abstractmethodinvocations,        ArrayList<javaMM_TypeAccess> javamm_typeaccesss    ) {
        this.javamm_singlevariabledeclarations = javamm_singlevariabledeclarations;
        this.javamm_typeparameters = javamm_typeparameters;
        this.javamm_methodrefs = javamm_methodrefs;
        this.javamm_abstractmethodinvocations = javamm_abstractmethodinvocations;
        this.javamm_typeaccesss = javamm_typeaccesss;
    }


    public List<javaMM_SingleVariableDeclaration> getJavamm_singlevariabledeclarations() {
        return javamm_singlevariabledeclarations;
    }

    public void addJavamm_singlevariabledeclaration(Javamm_singlevariabledeclaration javamm_singlevariabledeclaration) {
        this.javamm_singlevariabledeclarations.add(javamm_singlevariabledeclaration);
    }
    public javaMM_AbstractMethodInvocation getJavamm_abstractmethodinvocation() {
        return javamm_abstractmethodinvocation;
    }

    public void setJavamm_abstractmethodinvocation(javaMM_AbstractMethodInvocation javamm_abstractmethodinvocation) {
        this.javamm_abstractmethodinvocation = javamm_abstractmethodinvocation;
    }
    public List<javaMM_TypeParameter> getJavamm_typeparameters() {
        return javamm_typeparameters;
    }

    public void addJavamm_typeparameter(Javamm_typeparameter javamm_typeparameter) {
        this.javamm_typeparameters.add(javamm_typeparameter);
    }
    public List<javaMM_MethodRef> getJavamm_methodrefs() {
        return javamm_methodrefs;
    }

    public void addJavamm_methodref(Javamm_methodref javamm_methodref) {
        this.javamm_methodrefs.add(javamm_methodref);
    }
    public javaMM_MethodRef getJavamm_methodref() {
        return javamm_methodref;
    }

    public void setJavamm_methodref(javaMM_MethodRef javamm_methodref) {
        this.javamm_methodref = javamm_methodref;
    }
    public javaMM_SingleVariableDeclaration getJavamm_singlevariabledeclaration() {
        return javamm_singlevariabledeclaration;
    }

    public void setJavamm_singlevariabledeclaration(javaMM_SingleVariableDeclaration javamm_singlevariabledeclaration) {
        this.javamm_singlevariabledeclaration = javamm_singlevariabledeclaration;
    }
    public List<javaMM_AbstractMethodInvocation> getJavamm_abstractmethodinvocations() {
        return javamm_abstractmethodinvocations;
    }

    public void addJavamm_abstractmethodinvocation(Javamm_abstractmethodinvocation javamm_abstractmethodinvocation) {
        this.javamm_abstractmethodinvocations.add(javamm_abstractmethodinvocation);
    }
    public List<javaMM_TypeAccess> getJavamm_typeaccesss() {
        return javamm_typeaccesss;
    }

    public void addJavamm_typeaccess(Javamm_typeaccess javamm_typeaccess) {
        this.javamm_typeaccesss.add(javamm_typeaccess);
    }

}