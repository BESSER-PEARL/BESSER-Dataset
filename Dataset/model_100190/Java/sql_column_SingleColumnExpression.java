





import java.util.List;
import java.util.ArrayList;

public class sql_column_SingleColumnExpression  {

    private String alias;





    private parameter_SelectParameter parameter_selectparameter;


    public sql_column_SingleColumnExpression(
        String alias    ) {
        this.alias = alias;
    }


    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }

    public parameter_SelectParameter getParameter_selectparameter() {
        return parameter_selectparameter;
    }

    public void setParameter_selectparameter(parameter_SelectParameter parameter_selectparameter) {
        this.parameter_selectparameter = parameter_selectparameter;
    }

}