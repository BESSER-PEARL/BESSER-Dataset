





import java.util.List;
import java.util.ArrayList;

public class stext_OperationCall extends Expression {






    private List<stext_Expression> stext_expressions;


    public stext_OperationCall(
    ) {
        super(
        );
        this.stext_expressions = new ArrayList<>();
    }

    public stext_OperationCall(
        ArrayList<stext_Expression> stext_expressions    ) {
        this.stext_expressions = stext_expressions;
    }


    public List<stext_Expression> getStext_expressions() {
        return stext_expressions;
    }

    public void addStext_expression(Stext_expression stext_expression) {
        this.stext_expressions.add(stext_expression);
    }

}