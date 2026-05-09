





import java.util.List;
import java.util.ArrayList;

public class java_TypeAccess extends Expression, NamespaceAccess {






    private java_Type java_type;




    private java_ClassDeclaration java_classdeclaration;




    private java_MemberRef java_memberref;




    private java_Type java_type;




    private java_MethodRefParameter java_methodrefparameter;




    private java_NamespaceAccess java_namespaceaccess;




    private java_InstanceofExpression java_instanceofexpression;




    private java_SingleVariableDeclaration java_singlevariabledeclaration;




    private java_MethodDeclaration java_methoddeclaration;


    public java_TypeAccess(
    ) {
        super(
        );
    }



    public java_Type getJava_type() {
        return java_type;
    }

    public void setJava_type(java_Type java_type) {
        this.java_type = java_type;
    }
    public java_ClassDeclaration getJava_classdeclaration() {
        return java_classdeclaration;
    }

    public void setJava_classdeclaration(java_ClassDeclaration java_classdeclaration) {
        this.java_classdeclaration = java_classdeclaration;
    }
    public java_MemberRef getJava_memberref() {
        return java_memberref;
    }

    public void setJava_memberref(java_MemberRef java_memberref) {
        this.java_memberref = java_memberref;
    }
    public java_Type getJava_type() {
        return java_type;
    }

    public void setJava_type(java_Type java_type) {
        this.java_type = java_type;
    }
    public java_MethodRefParameter getJava_methodrefparameter() {
        return java_methodrefparameter;
    }

    public void setJava_methodrefparameter(java_MethodRefParameter java_methodrefparameter) {
        this.java_methodrefparameter = java_methodrefparameter;
    }
    public java_NamespaceAccess getJava_namespaceaccess() {
        return java_namespaceaccess;
    }

    public void setJava_namespaceaccess(java_NamespaceAccess java_namespaceaccess) {
        this.java_namespaceaccess = java_namespaceaccess;
    }
    public java_InstanceofExpression getJava_instanceofexpression() {
        return java_instanceofexpression;
    }

    public void setJava_instanceofexpression(java_InstanceofExpression java_instanceofexpression) {
        this.java_instanceofexpression = java_instanceofexpression;
    }
    public java_SingleVariableDeclaration getJava_singlevariabledeclaration() {
        return java_singlevariabledeclaration;
    }

    public void setJava_singlevariabledeclaration(java_SingleVariableDeclaration java_singlevariabledeclaration) {
        this.java_singlevariabledeclaration = java_singlevariabledeclaration;
    }
    public java_MethodDeclaration getJava_methoddeclaration() {
        return java_methoddeclaration;
    }

    public void setJava_methoddeclaration(java_MethodDeclaration java_methoddeclaration) {
        this.java_methoddeclaration = java_methoddeclaration;
    }

}