





import java.util.List;
import java.util.ArrayList;

public class eol_VariableDeclarationExpression extends Expression {

    private String lastDefinitionPoint;





    private eol_NameExpression eol_nameexpression;




    private List<eol_Expression> eol_expressions;


    public eol_VariableDeclarationExpression(
        String lastDefinitionPoint    ) {
        super(
        );
        this.lastDefinitionPoint = lastDefinitionPoint;
        this.eol_expressions = new ArrayList<>();
    }

    public eol_VariableDeclarationExpression(
        String lastDefinitionPoint        ArrayList<eol_Expression> eol_expressions    ) {
        this.lastDefinitionPoint = lastDefinitionPoint;
        this.eol_expressions = eol_expressions;
    }

    public String getLastdefinitionpoint() {
        return lastDefinitionPoint;
    }

    public void setLastdefinitionpoint(String lastDefinitionPoint) {
        this.lastDefinitionPoint = lastDefinitionPoint;
    }

    public eol_NameExpression getEol_nameexpression() {
        return eol_nameexpression;
    }

    public void setEol_nameexpression(eol_NameExpression eol_nameexpression) {
        this.eol_nameexpression = eol_nameexpression;
    }
    public List<eol_Expression> getEol_expressions() {
        return eol_expressions;
    }

    public void addEol_expression(Eol_expression eol_expression) {
        this.eol_expressions.add(eol_expression);
    }

}