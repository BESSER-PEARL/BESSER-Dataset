





import java.util.List;
import java.util.ArrayList;

public class logoASM_ProcCall extends Expression {






    private List<logoASM_Expression> logoasm_expressions;




    private logoASM_ProcDeclaration logoasm_procdeclaration;


    public logoASM_ProcCall(
    ) {
        super(
        );
        this.logoasm_expressions = new ArrayList<>();
    }

    public logoASM_ProcCall(
        ArrayList<logoASM_Expression> logoasm_expressions    ) {
        this.logoasm_expressions = logoasm_expressions;
    }


    public List<logoASM_Expression> getLogoasm_expressions() {
        return logoasm_expressions;
    }

    public void addLogoasm_expression(Logoasm_expression logoasm_expression) {
        this.logoasm_expressions.add(logoasm_expression);
    }
    public logoASM_ProcDeclaration getLogoasm_procdeclaration() {
        return logoasm_procdeclaration;
    }

    public void setLogoasm_procdeclaration(logoASM_ProcDeclaration logoasm_procdeclaration) {
        this.logoasm_procdeclaration = logoasm_procdeclaration;
    }

}