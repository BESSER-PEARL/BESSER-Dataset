





import java.util.List;
import java.util.ArrayList;

public class java__AbstractMethodDeclaration extends BodyDeclaration {






    private List<java__TypeAccess> java__typeaccesss;




    private java__AbstractMethodInvocation java__abstractmethodinvocation;




    private List<java__MethodRef> java__methodrefs;




    private java__MethodRef java__methodref;




    private List<java__SingleVariableDeclaration> java__singlevariabledeclarations;




    private List<java__TypeParameter> java__typeparameters;




    private List<java__AbstractMethodInvocation> java__abstractmethodinvocations;




    private java__SingleVariableDeclaration java__singlevariabledeclaration;


    public java__AbstractMethodDeclaration(
    ) {
        super(
        );
        this.java__typeaccesss = new ArrayList<>();
        this.java__methodrefs = new ArrayList<>();
        this.java__singlevariabledeclarations = new ArrayList<>();
        this.java__typeparameters = new ArrayList<>();
        this.java__abstractmethodinvocations = new ArrayList<>();
    }

    public java__AbstractMethodDeclaration(
        ArrayList<java__TypeAccess> java__typeaccesss,        ArrayList<java__MethodRef> java__methodrefs,        ArrayList<java__SingleVariableDeclaration> java__singlevariabledeclarations,        ArrayList<java__TypeParameter> java__typeparameters,        ArrayList<java__AbstractMethodInvocation> java__abstractmethodinvocations    ) {
        this.java__typeaccesss = java__typeaccesss;
        this.java__methodrefs = java__methodrefs;
        this.java__singlevariabledeclarations = java__singlevariabledeclarations;
        this.java__typeparameters = java__typeparameters;
        this.java__abstractmethodinvocations = java__abstractmethodinvocations;
    }


    public List<java__TypeAccess> getJava__typeaccesss() {
        return java__typeaccesss;
    }

    public void addJava__typeaccess(Java__typeaccess java__typeaccess) {
        this.java__typeaccesss.add(java__typeaccess);
    }
    public java__AbstractMethodInvocation getJava__abstractmethodinvocation() {
        return java__abstractmethodinvocation;
    }

    public void setJava__abstractmethodinvocation(java__AbstractMethodInvocation java__abstractmethodinvocation) {
        this.java__abstractmethodinvocation = java__abstractmethodinvocation;
    }
    public List<java__MethodRef> getJava__methodrefs() {
        return java__methodrefs;
    }

    public void addJava__methodref(Java__methodref java__methodref) {
        this.java__methodrefs.add(java__methodref);
    }
    public java__MethodRef getJava__methodref() {
        return java__methodref;
    }

    public void setJava__methodref(java__MethodRef java__methodref) {
        this.java__methodref = java__methodref;
    }
    public List<java__SingleVariableDeclaration> getJava__singlevariabledeclarations() {
        return java__singlevariabledeclarations;
    }

    public void addJava__singlevariabledeclaration(Java__singlevariabledeclaration java__singlevariabledeclaration) {
        this.java__singlevariabledeclarations.add(java__singlevariabledeclaration);
    }
    public List<java__TypeParameter> getJava__typeparameters() {
        return java__typeparameters;
    }

    public void addJava__typeparameter(Java__typeparameter java__typeparameter) {
        this.java__typeparameters.add(java__typeparameter);
    }
    public List<java__AbstractMethodInvocation> getJava__abstractmethodinvocations() {
        return java__abstractmethodinvocations;
    }

    public void addJava__abstractmethodinvocation(Java__abstractmethodinvocation java__abstractmethodinvocation) {
        this.java__abstractmethodinvocations.add(java__abstractmethodinvocation);
    }
    public java__SingleVariableDeclaration getJava__singlevariabledeclaration() {
        return java__singlevariabledeclaration;
    }

    public void setJava__singlevariabledeclaration(java__SingleVariableDeclaration java__singlevariabledeclaration) {
        this.java__singlevariabledeclaration = java__singlevariabledeclaration;
    }

}