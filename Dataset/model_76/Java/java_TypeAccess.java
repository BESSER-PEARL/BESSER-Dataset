





import java.util.List;
import java.util.ArrayList;

public class java_TypeAccess extends Expression, NamespaceAccess {






    private java_Annotation java_annotation;




    private java_MethodRef java_methodref;




    private java_CastExpression java_castexpression;




    private java_AbstractTypeQualifiedExpression java_abstracttypequalifiedexpression;




    private java_TypeParameter java_typeparameter;




    private java_ArrayCreation java_arraycreation;




    private java_TypeLiteral java_typeliteral;




    private java_ClassInstanceCreation java_classinstancecreation;




    private java_InstanceofExpression java_instanceofexpression;


    public java_TypeAccess(
    ) {
        super(
        );
    }



    public java_Annotation getJava_annotation() {
        return java_annotation;
    }

    public void setJava_annotation(java_Annotation java_annotation) {
        this.java_annotation = java_annotation;
    }
    public java_MethodRef getJava_methodref() {
        return java_methodref;
    }

    public void setJava_methodref(java_MethodRef java_methodref) {
        this.java_methodref = java_methodref;
    }
    public java_CastExpression getJava_castexpression() {
        return java_castexpression;
    }

    public void setJava_castexpression(java_CastExpression java_castexpression) {
        this.java_castexpression = java_castexpression;
    }
    public java_AbstractTypeQualifiedExpression getJava_abstracttypequalifiedexpression() {
        return java_abstracttypequalifiedexpression;
    }

    public void setJava_abstracttypequalifiedexpression(java_AbstractTypeQualifiedExpression java_abstracttypequalifiedexpression) {
        this.java_abstracttypequalifiedexpression = java_abstracttypequalifiedexpression;
    }
    public java_TypeParameter getJava_typeparameter() {
        return java_typeparameter;
    }

    public void setJava_typeparameter(java_TypeParameter java_typeparameter) {
        this.java_typeparameter = java_typeparameter;
    }
    public java_ArrayCreation getJava_arraycreation() {
        return java_arraycreation;
    }

    public void setJava_arraycreation(java_ArrayCreation java_arraycreation) {
        this.java_arraycreation = java_arraycreation;
    }
    public java_TypeLiteral getJava_typeliteral() {
        return java_typeliteral;
    }

    public void setJava_typeliteral(java_TypeLiteral java_typeliteral) {
        this.java_typeliteral = java_typeliteral;
    }
    public java_ClassInstanceCreation getJava_classinstancecreation() {
        return java_classinstancecreation;
    }

    public void setJava_classinstancecreation(java_ClassInstanceCreation java_classinstancecreation) {
        this.java_classinstancecreation = java_classinstancecreation;
    }
    public java_InstanceofExpression getJava_instanceofexpression() {
        return java_instanceofexpression;
    }

    public void setJava_instanceofexpression(java_InstanceofExpression java_instanceofexpression) {
        this.java_instanceofexpression = java_instanceofexpression;
    }

}