





import java.util.List;
import java.util.ArrayList;

public class java_InstanceSpecification extends NamedElement {






    private List<java_AbstractMethodInvocation> java_abstractmethodinvocations;




    private java_Type java_type;




    private java_Expression java_expression;




    private java_Type java_type;


    public java_InstanceSpecification(
    ) {
        super(
        );
        this.java_abstractmethodinvocations = new ArrayList<>();
    }

    public java_InstanceSpecification(
        ArrayList<java_AbstractMethodInvocation> java_abstractmethodinvocations    ) {
        this.java_abstractmethodinvocations = java_abstractmethodinvocations;
    }


    public List<java_AbstractMethodInvocation> getJava_abstractmethodinvocations() {
        return java_abstractmethodinvocations;
    }

    public void addJava_abstractmethodinvocation(Java_abstractmethodinvocation java_abstractmethodinvocation) {
        this.java_abstractmethodinvocations.add(java_abstractmethodinvocation);
    }
    public java_Type getJava_type() {
        return java_type;
    }

    public void setJava_type(java_Type java_type) {
        this.java_type = java_type;
    }
    public java_Expression getJava_expression() {
        return java_expression;
    }

    public void setJava_expression(java_Expression java_expression) {
        this.java_expression = java_expression;
    }
    public java_Type getJava_type() {
        return java_type;
    }

    public void setJava_type(java_Type java_type) {
        this.java_type = java_type;
    }

}