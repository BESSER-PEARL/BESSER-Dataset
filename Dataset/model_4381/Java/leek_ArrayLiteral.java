





import java.util.List;
import java.util.ArrayList;

public class leek_ArrayLiteral extends Expression {






    private List<leek_Expression> leek_expressions;


    public leek_ArrayLiteral(
    ) {
        super(
        );
        this.leek_expressions = new ArrayList<>();
    }

    public leek_ArrayLiteral(
        ArrayList<leek_Expression> leek_expressions    ) {
        this.leek_expressions = leek_expressions;
    }


    public List<leek_Expression> getLeek_expressions() {
        return leek_expressions;
    }

    public void addLeek_expression(Leek_expression leek_expression) {
        this.leek_expressions.add(leek_expression);
    }

}