





import java.util.List;
import java.util.ArrayList;

public class ale_OrderedSet extends literal {






    private List<ale_Expression> ale_expressions;


    public ale_OrderedSet(
    ) {
        super(
        );
        this.ale_expressions = new ArrayList<>();
    }

    public ale_OrderedSet(
        ArrayList<ale_Expression> ale_expressions    ) {
        this.ale_expressions = ale_expressions;
    }


    public List<ale_Expression> getAle_expressions() {
        return ale_expressions;
    }

    public void addAle_expression(Ale_expression ale_expression) {
        this.ale_expressions.add(ale_expression);
    }

}