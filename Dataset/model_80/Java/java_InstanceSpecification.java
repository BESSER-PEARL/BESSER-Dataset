





import java.util.List;
import java.util.ArrayList;

public class java_InstanceSpecification extends NamedElement {






    private java_Expression java_expression;




    private List<java_AbstractMethodInvocation> java_abstractmethodinvocations;


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


    public java_Expression getJava_expression() {
        return java_expression;
    }

    public void setJava_expression(java_Expression java_expression) {
        this.java_expression = java_expression;
    }
    public List<java_AbstractMethodInvocation> getJava_abstractmethodinvocations() {
        return java_abstractmethodinvocations;
    }

    public void addJava_abstractmethodinvocation(Java_abstractmethodinvocation java_abstractmethodinvocation) {
        this.java_abstractmethodinvocations.add(java_abstractmethodinvocation);
    }

}