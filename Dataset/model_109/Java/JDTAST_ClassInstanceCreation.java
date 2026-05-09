





import java.util.List;
import java.util.ArrayList;

public class JDTAST_ClassInstanceCreation extends Expression {






    private JDTAST_Expression jdtast_expression;




    private List<JDTAST_Type> jdtast_types;




    private JDTAST_Type jdtast_type;




    private JDTAST_AnonymousClassDeclaration jdtast_anonymousclassdeclaration;




    private List<JDTAST_Expression> jdtast_expressions;


    public JDTAST_ClassInstanceCreation(
    ) {
        super(
        );
        this.jdtast_types = new ArrayList<>();
        this.jdtast_expressions = new ArrayList<>();
    }

    public JDTAST_ClassInstanceCreation(
        ArrayList<JDTAST_Type> jdtast_types,        ArrayList<JDTAST_Expression> jdtast_expressions    ) {
        this.jdtast_types = jdtast_types;
        this.jdtast_expressions = jdtast_expressions;
    }


    public JDTAST_Expression getJdtast_expression() {
        return jdtast_expression;
    }

    public void setJdtast_expression(JDTAST_Expression jdtast_expression) {
        this.jdtast_expression = jdtast_expression;
    }
    public List<JDTAST_Type> getJdtast_types() {
        return jdtast_types;
    }

    public void addJdtast_type(Jdtast_type jdtast_type) {
        this.jdtast_types.add(jdtast_type);
    }
    public JDTAST_Type getJdtast_type() {
        return jdtast_type;
    }

    public void setJdtast_type(JDTAST_Type jdtast_type) {
        this.jdtast_type = jdtast_type;
    }
    public JDTAST_AnonymousClassDeclaration getJdtast_anonymousclassdeclaration() {
        return jdtast_anonymousclassdeclaration;
    }

    public void setJdtast_anonymousclassdeclaration(JDTAST_AnonymousClassDeclaration jdtast_anonymousclassdeclaration) {
        this.jdtast_anonymousclassdeclaration = jdtast_anonymousclassdeclaration;
    }
    public List<JDTAST_Expression> getJdtast_expressions() {
        return jdtast_expressions;
    }

    public void addJdtast_expression(Jdtast_expression jdtast_expression) {
        this.jdtast_expressions.add(jdtast_expression);
    }

}