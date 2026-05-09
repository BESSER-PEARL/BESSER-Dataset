





import java.util.List;
import java.util.ArrayList;

public class java_EnumConstantDeclaration extends BodyDeclaration, VariableDeclaration {






    private java_AnonymousClassDeclaration java_anonymousclassdeclaration;




    private List<java_Expression> java_expressions;


    public java_EnumConstantDeclaration(
    ) {
        super(
        );
        this.java_expressions = new ArrayList<>();
    }

    public java_EnumConstantDeclaration(
        ArrayList<java_Expression> java_expressions    ) {
        this.java_expressions = java_expressions;
    }


    public java_AnonymousClassDeclaration getJava_anonymousclassdeclaration() {
        return java_anonymousclassdeclaration;
    }

    public void setJava_anonymousclassdeclaration(java_AnonymousClassDeclaration java_anonymousclassdeclaration) {
        this.java_anonymousclassdeclaration = java_anonymousclassdeclaration;
    }
    public List<java_Expression> getJava_expressions() {
        return java_expressions;
    }

    public void addJava_expression(Java_expression java_expression) {
        this.java_expressions.add(java_expression);
    }

}