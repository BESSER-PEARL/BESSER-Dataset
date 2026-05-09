





import java.util.List;
import java.util.ArrayList;

public class java_AbstractMethodDeclaration extends BodyDeclaration {






    private java_AbstractMethodInvocation java_abstractmethodinvocation;




    private List<java_TypeAccess> java_typeaccesss;




    private List<java_MethodRef> java_methodrefs;




    private java_Block java_block;




    private List<java_AbstractMethodInvocation> java_abstractmethodinvocations;




    private List<java_TypeParameter> java_typeparameters;




    private java_MethodRef java_methodref;




    private List<java_SingleVariableDeclaration> java_singlevariabledeclarations;




    private java_SingleVariableDeclaration java_singlevariabledeclaration;


    public java_AbstractMethodDeclaration(
    ) {
        super(
        );
        this.java_typeaccesss = new ArrayList<>();
        this.java_methodrefs = new ArrayList<>();
        this.java_abstractmethodinvocations = new ArrayList<>();
        this.java_typeparameters = new ArrayList<>();
        this.java_singlevariabledeclarations = new ArrayList<>();
    }

    public java_AbstractMethodDeclaration(
        ArrayList<java_TypeAccess> java_typeaccesss,        ArrayList<java_MethodRef> java_methodrefs,        ArrayList<java_AbstractMethodInvocation> java_abstractmethodinvocations,        ArrayList<java_TypeParameter> java_typeparameters,        ArrayList<java_SingleVariableDeclaration> java_singlevariabledeclarations    ) {
        this.java_typeaccesss = java_typeaccesss;
        this.java_methodrefs = java_methodrefs;
        this.java_abstractmethodinvocations = java_abstractmethodinvocations;
        this.java_typeparameters = java_typeparameters;
        this.java_singlevariabledeclarations = java_singlevariabledeclarations;
    }


    public java_AbstractMethodInvocation getJava_abstractmethodinvocation() {
        return java_abstractmethodinvocation;
    }

    public void setJava_abstractmethodinvocation(java_AbstractMethodInvocation java_abstractmethodinvocation) {
        this.java_abstractmethodinvocation = java_abstractmethodinvocation;
    }
    public List<java_TypeAccess> getJava_typeaccesss() {
        return java_typeaccesss;
    }

    public void addJava_typeaccess(Java_typeaccess java_typeaccess) {
        this.java_typeaccesss.add(java_typeaccess);
    }
    public List<java_MethodRef> getJava_methodrefs() {
        return java_methodrefs;
    }

    public void addJava_methodref(Java_methodref java_methodref) {
        this.java_methodrefs.add(java_methodref);
    }
    public java_Block getJava_block() {
        return java_block;
    }

    public void setJava_block(java_Block java_block) {
        this.java_block = java_block;
    }
    public List<java_AbstractMethodInvocation> getJava_abstractmethodinvocations() {
        return java_abstractmethodinvocations;
    }

    public void addJava_abstractmethodinvocation(Java_abstractmethodinvocation java_abstractmethodinvocation) {
        this.java_abstractmethodinvocations.add(java_abstractmethodinvocation);
    }
    public List<java_TypeParameter> getJava_typeparameters() {
        return java_typeparameters;
    }

    public void addJava_typeparameter(Java_typeparameter java_typeparameter) {
        this.java_typeparameters.add(java_typeparameter);
    }
    public java_MethodRef getJava_methodref() {
        return java_methodref;
    }

    public void setJava_methodref(java_MethodRef java_methodref) {
        this.java_methodref = java_methodref;
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

}