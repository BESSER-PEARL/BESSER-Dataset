





import java.util.List;
import java.util.ArrayList;

public class rankPL_FunctionCall extends Expression {






    private List<rankPL_Expression> rankpl_expressions;




    private rankPL_AbstractDefinition rankpl_abstractdefinition;


    public rankPL_FunctionCall(
    ) {
        super(
        );
        this.rankpl_expressions = new ArrayList<>();
    }

    public rankPL_FunctionCall(
        ArrayList<rankPL_Expression> rankpl_expressions    ) {
        this.rankpl_expressions = rankpl_expressions;
    }


    public List<rankPL_Expression> getRankpl_expressions() {
        return rankpl_expressions;
    }

    public void addRankpl_expression(Rankpl_expression rankpl_expression) {
        this.rankpl_expressions.add(rankpl_expression);
    }
    public rankPL_AbstractDefinition getRankpl_abstractdefinition() {
        return rankpl_abstractdefinition;
    }

    public void setRankpl_abstractdefinition(rankPL_AbstractDefinition rankpl_abstractdefinition) {
        this.rankpl_abstractdefinition = rankpl_abstractdefinition;
    }

}