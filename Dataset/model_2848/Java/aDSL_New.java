





import java.util.List;
import java.util.ArrayList;

public class aDSL_New extends Expression {






    private aDSL_VariableType adsl_variabletype;




    private List<aDSL_Expression> adsl_expressions;


    public aDSL_New(
    ) {
        super(
        );
        this.adsl_expressions = new ArrayList<>();
    }

    public aDSL_New(
        ArrayList<aDSL_Expression> adsl_expressions    ) {
        this.adsl_expressions = adsl_expressions;
    }


    public aDSL_VariableType getAdsl_variabletype() {
        return adsl_variabletype;
    }

    public void setAdsl_variabletype(aDSL_VariableType adsl_variabletype) {
        this.adsl_variabletype = adsl_variabletype;
    }
    public List<aDSL_Expression> getAdsl_expressions() {
        return adsl_expressions;
    }

    public void addAdsl_expression(Adsl_expression adsl_expression) {
        this.adsl_expressions.add(adsl_expression);
    }

}