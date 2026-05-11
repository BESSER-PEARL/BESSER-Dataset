





import java.util.List;
import java.util.ArrayList;

public class logiclanguage_QuantifiedExpression extends Term {






    private List<logiclanguage_Variable> logiclanguage_variables;


    public logiclanguage_QuantifiedExpression(
    ) {
        super(
        );
        this.logiclanguage_variables = new ArrayList<>();
    }

    public logiclanguage_QuantifiedExpression(
        ArrayList<logiclanguage_Variable> logiclanguage_variables    ) {
        this.logiclanguage_variables = logiclanguage_variables;
    }


    public List<logiclanguage_Variable> getLogiclanguage_variables() {
        return logiclanguage_variables;
    }

    public void addLogiclanguage_variable(Logiclanguage_variable logiclanguage_variable) {
        this.logiclanguage_variables.add(logiclanguage_variable);
    }

}