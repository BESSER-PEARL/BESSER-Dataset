





import java.util.List;
import java.util.ArrayList;

public class JDTAST_EnumConstantDeclaration extends BodyDeclaration {






    private JDTAST_SimpleName jdtast_simplename;




    private List<JDTAST_Expression> jdtast_expressions;




    private JDTAST_AnonymousClassDeclaration jdtast_anonymousclassdeclaration;


    public JDTAST_EnumConstantDeclaration(
    ) {
        super(
        );
        this.jdtast_expressions = new ArrayList<>();
    }

    public JDTAST_EnumConstantDeclaration(
        ArrayList<JDTAST_Expression> jdtast_expressions    ) {
        this.jdtast_expressions = jdtast_expressions;
    }


    public JDTAST_SimpleName getJdtast_simplename() {
        return jdtast_simplename;
    }

    public void setJdtast_simplename(JDTAST_SimpleName jdtast_simplename) {
        this.jdtast_simplename = jdtast_simplename;
    }
    public List<JDTAST_Expression> getJdtast_expressions() {
        return jdtast_expressions;
    }

    public void addJdtast_expression(Jdtast_expression jdtast_expression) {
        this.jdtast_expressions.add(jdtast_expression);
    }
    public JDTAST_AnonymousClassDeclaration getJdtast_anonymousclassdeclaration() {
        return jdtast_anonymousclassdeclaration;
    }

    public void setJdtast_anonymousclassdeclaration(JDTAST_AnonymousClassDeclaration jdtast_anonymousclassdeclaration) {
        this.jdtast_anonymousclassdeclaration = jdtast_anonymousclassdeclaration;
    }

}