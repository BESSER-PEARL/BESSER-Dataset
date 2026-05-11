





import java.util.List;
import java.util.ArrayList;

public class umlTrace_BasicBehaviors_TracedParameterValue  {






    private List<ParameterValue_values_ParameterValue_Value> parametervalue_values_parametervalue_values;




    private List<ParameterValue_parameter_ParameterValue_Value> parametervalue_parameter_parametervalue_values;


    public umlTrace_BasicBehaviors_TracedParameterValue(
    ) {
        this.parametervalue_values_parametervalue_values = new ArrayList<>();
        this.parametervalue_parameter_parametervalue_values = new ArrayList<>();
    }

    public umlTrace_BasicBehaviors_TracedParameterValue(
        ArrayList<ParameterValue_values_ParameterValue_Value> parametervalue_values_parametervalue_values,        ArrayList<ParameterValue_parameter_ParameterValue_Value> parametervalue_parameter_parametervalue_values    ) {
        this.parametervalue_values_parametervalue_values = parametervalue_values_parametervalue_values;
        this.parametervalue_parameter_parametervalue_values = parametervalue_parameter_parametervalue_values;
    }


    public List<ParameterValue_values_ParameterValue_Value> getParametervalue_values_parametervalue_values() {
        return parametervalue_values_parametervalue_values;
    }

    public void addParametervalue_values_parametervalue_value(Parametervalue_values_parametervalue_value parametervalue_values_parametervalue_value) {
        this.parametervalue_values_parametervalue_values.add(parametervalue_values_parametervalue_value);
    }
    public List<ParameterValue_parameter_ParameterValue_Value> getParametervalue_parameter_parametervalue_values() {
        return parametervalue_parameter_parametervalue_values;
    }

    public void addParametervalue_parameter_parametervalue_value(Parametervalue_parameter_parametervalue_value parametervalue_parameter_parametervalue_value) {
        this.parametervalue_parameter_parametervalue_values.add(parametervalue_parameter_parametervalue_value);
    }

}