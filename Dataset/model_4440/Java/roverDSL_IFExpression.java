





import java.util.List;
import java.util.ArrayList;

public class roverDSL_IFExpression extends Expression {






    private List<roverDSL_Expression> roverdsl_expressions;




    private roverDSL_ValueExpression roverdsl_valueexpression;




    private List<roverDSL_Expression> roverdsl_expressions;


    public roverDSL_IFExpression(
    ) {
        super(
        );
        this.roverdsl_expressions = new ArrayList<>();
        this.roverdsl_expressions = new ArrayList<>();
    }

    public roverDSL_IFExpression(
        ArrayList<roverDSL_Expression> roverdsl_expressions,        ArrayList<roverDSL_Expression> roverdsl_expressions    ) {
        this.roverdsl_expressions = roverdsl_expressions;
        this.roverdsl_expressions = roverdsl_expressions;
    }


    public List<roverDSL_Expression> getRoverdsl_expressions() {
        return roverdsl_expressions;
    }

    public void addRoverdsl_expression(Roverdsl_expression roverdsl_expression) {
        this.roverdsl_expressions.add(roverdsl_expression);
    }
    public roverDSL_ValueExpression getRoverdsl_valueexpression() {
        return roverdsl_valueexpression;
    }

    public void setRoverdsl_valueexpression(roverDSL_ValueExpression roverdsl_valueexpression) {
        this.roverdsl_valueexpression = roverdsl_valueexpression;
    }
    public List<roverDSL_Expression> getRoverdsl_expressions() {
        return roverdsl_expressions;
    }

    public void addRoverdsl_expression(Roverdsl_expression roverdsl_expression) {
        this.roverdsl_expressions.add(roverdsl_expression);
    }

}