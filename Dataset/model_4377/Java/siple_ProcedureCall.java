





import java.util.List;
import java.util.ArrayList;

public class siple_ProcedureCall extends Expression {






    private siple_ProcedureDeclaration siple_proceduredeclaration;




    private List<siple_Expression> siple_expressions;




    private siple_Expression siple_expression;


    public siple_ProcedureCall(
    ) {
        super(
        );
        this.siple_expressions = new ArrayList<>();
    }

    public siple_ProcedureCall(
        ArrayList<siple_Expression> siple_expressions    ) {
        this.siple_expressions = siple_expressions;
    }


    public siple_ProcedureDeclaration getSiple_proceduredeclaration() {
        return siple_proceduredeclaration;
    }

    public void setSiple_proceduredeclaration(siple_ProcedureDeclaration siple_proceduredeclaration) {
        this.siple_proceduredeclaration = siple_proceduredeclaration;
    }
    public List<siple_Expression> getSiple_expressions() {
        return siple_expressions;
    }

    public void addSiple_expression(Siple_expression siple_expression) {
        this.siple_expressions.add(siple_expression);
    }
    public siple_Expression getSiple_expression() {
        return siple_expression;
    }

    public void setSiple_expression(siple_Expression siple_expression) {
        this.siple_expression = siple_expression;
    }

}