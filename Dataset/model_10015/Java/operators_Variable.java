





import java.util.List;
import java.util.ArrayList;

public class operators_Variable  {

    private String name;





    private operators_VariableReference operators_variablereference;


    public operators_Variable(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public operators_VariableReference getOperators_variablereference() {
        return operators_variablereference;
    }

    public void setOperators_variablereference(operators_VariableReference operators_variablereference) {
        this.operators_variablereference = operators_variablereference;
    }

}