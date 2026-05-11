





import java.util.List;
import java.util.ArrayList;

public class umlTrace_Input_TracedInputParameterValues  {






    private List<InputParameterValues_parameterValues_Value> inputparametervalues_parametervalues_values;




    private List<InputParameterValues_name_Value> inputparametervalues_name_values;


    public umlTrace_Input_TracedInputParameterValues(
    ) {
        this.inputparametervalues_parametervalues_values = new ArrayList<>();
        this.inputparametervalues_name_values = new ArrayList<>();
    }

    public umlTrace_Input_TracedInputParameterValues(
        ArrayList<InputParameterValues_parameterValues_Value> inputparametervalues_parametervalues_values,        ArrayList<InputParameterValues_name_Value> inputparametervalues_name_values    ) {
        this.inputparametervalues_parametervalues_values = inputparametervalues_parametervalues_values;
        this.inputparametervalues_name_values = inputparametervalues_name_values;
    }


    public List<InputParameterValues_parameterValues_Value> getInputparametervalues_parametervalues_values() {
        return inputparametervalues_parametervalues_values;
    }

    public void addInputparametervalues_parametervalues_value(Inputparametervalues_parametervalues_value inputparametervalues_parametervalues_value) {
        this.inputparametervalues_parametervalues_values.add(inputparametervalues_parametervalues_value);
    }
    public List<InputParameterValues_name_Value> getInputparametervalues_name_values() {
        return inputparametervalues_name_values;
    }

    public void addInputparametervalues_name_value(Inputparametervalues_name_value inputparametervalues_name_value) {
        this.inputparametervalues_name_values.add(inputparametervalues_name_value);
    }

}