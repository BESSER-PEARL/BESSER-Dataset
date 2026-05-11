





import java.util.List;
import java.util.ArrayList;

public class ilp_Variable  {

    private String dataType;
    private String name;





    private ilp_IntegerLinearProgram ilp_integerlinearprogram;




    private ilp_VariableExpression ilp_variableexpression;


    public ilp_Variable(
        String dataType,        String name    ) {
        this.dataType = dataType;
        this.name = name;
    }


    public String getDatatype() {
        return dataType;
    }

    public void setDatatype(String dataType) {
        this.dataType = dataType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ilp_IntegerLinearProgram getIlp_integerlinearprogram() {
        return ilp_integerlinearprogram;
    }

    public void setIlp_integerlinearprogram(ilp_IntegerLinearProgram ilp_integerlinearprogram) {
        this.ilp_integerlinearprogram = ilp_integerlinearprogram;
    }
    public ilp_VariableExpression getIlp_variableexpression() {
        return ilp_variableexpression;
    }

    public void setIlp_variableexpression(ilp_VariableExpression ilp_variableexpression) {
        this.ilp_variableexpression = ilp_variableexpression;
    }

}