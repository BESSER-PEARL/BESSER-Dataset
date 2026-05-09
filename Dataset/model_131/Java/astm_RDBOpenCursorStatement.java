





import java.util.List;
import java.util.ArrayList;

public class astm_RDBOpenCursorStatement extends RDBCursorStatement {






    private List<astm_Expression> astm_expressions;


    public astm_RDBOpenCursorStatement(
    ) {
        super(
        );
        this.astm_expressions = new ArrayList<>();
    }

    public astm_RDBOpenCursorStatement(
        ArrayList<astm_Expression> astm_expressions    ) {
        this.astm_expressions = astm_expressions;
    }


    public List<astm_Expression> getAstm_expressions() {
        return astm_expressions;
    }

    public void addAstm_expression(Astm_expression astm_expression) {
        this.astm_expressions.add(astm_expression);
    }

}