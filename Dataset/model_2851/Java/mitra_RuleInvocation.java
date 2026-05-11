





import java.util.List;
import java.util.ArrayList;

public class mitra_RuleInvocation extends TerminalExpression, StatementExpression {






    private mitra_RuleDeclaration mitra_ruledeclaration;




    private List<mitra_Expression> mitra_expressions;


    public mitra_RuleInvocation(
    ) {
        super(
        );
        this.mitra_expressions = new ArrayList<>();
    }

    public mitra_RuleInvocation(
        ArrayList<mitra_Expression> mitra_expressions    ) {
        this.mitra_expressions = mitra_expressions;
    }


    public mitra_RuleDeclaration getMitra_ruledeclaration() {
        return mitra_ruledeclaration;
    }

    public void setMitra_ruledeclaration(mitra_RuleDeclaration mitra_ruledeclaration) {
        this.mitra_ruledeclaration = mitra_ruledeclaration;
    }
    public List<mitra_Expression> getMitra_expressions() {
        return mitra_expressions;
    }

    public void addMitra_expression(Mitra_expression mitra_expression) {
        this.mitra_expressions.add(mitra_expression);
    }

}