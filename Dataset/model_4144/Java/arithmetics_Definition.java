





import java.util.List;
import java.util.ArrayList;

public class arithmetics_Definition extends Statement, AbstractDefinition {






    private arithmetics_Expression arithmetics_expression;




    private List<arithmetics_DeclaredParameter> arithmetics_declaredparameters;


    public arithmetics_Definition(
    ) {
        super(
        );
        this.arithmetics_declaredparameters = new ArrayList<>();
    }

    public arithmetics_Definition(
        ArrayList<arithmetics_DeclaredParameter> arithmetics_declaredparameters    ) {
        this.arithmetics_declaredparameters = arithmetics_declaredparameters;
    }


    public arithmetics_Expression getArithmetics_expression() {
        return arithmetics_expression;
    }

    public void setArithmetics_expression(arithmetics_Expression arithmetics_expression) {
        this.arithmetics_expression = arithmetics_expression;
    }
    public List<arithmetics_DeclaredParameter> getArithmetics_declaredparameters() {
        return arithmetics_declaredparameters;
    }

    public void addArithmetics_declaredparameter(Arithmetics_declaredparameter arithmetics_declaredparameter) {
        this.arithmetics_declaredparameters.add(arithmetics_declaredparameter);
    }

}