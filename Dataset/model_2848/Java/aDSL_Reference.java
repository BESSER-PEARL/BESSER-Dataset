





import java.util.List;
import java.util.ArrayList;

public class aDSL_Reference extends Expression {

    private boolean isarray;





    private aDSL_VarDef adsl_vardef;




    private List<aDSL_Expression> adsl_expressions;


    public aDSL_Reference(
        boolean isarray    ) {
        super(
        );
        this.isarray = isarray;
        this.adsl_expressions = new ArrayList<>();
    }

    public aDSL_Reference(
        boolean isarray        ArrayList<aDSL_Expression> adsl_expressions    ) {
        this.isarray = isarray;
        this.adsl_expressions = adsl_expressions;
    }

    public boolean getIsarray() {
        return isarray;
    }

    public void setIsarray(boolean isarray) {
        this.isarray = isarray;
    }

    public aDSL_VarDef getAdsl_vardef() {
        return adsl_vardef;
    }

    public void setAdsl_vardef(aDSL_VarDef adsl_vardef) {
        this.adsl_vardef = adsl_vardef;
    }
    public List<aDSL_Expression> getAdsl_expressions() {
        return adsl_expressions;
    }

    public void addAdsl_expression(Adsl_expression adsl_expression) {
        this.adsl_expressions.add(adsl_expression);
    }

}