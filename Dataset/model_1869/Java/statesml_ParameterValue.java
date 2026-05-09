





import java.util.List;
import java.util.ArrayList;

public class statesml_ParameterValue  {






    private statesml_FunctionCall statesml_functioncall;




    private List<statesml_IncomingParameter> statesml_incomingparameters;


    public statesml_ParameterValue(
    ) {
        this.statesml_incomingparameters = new ArrayList<>();
    }

    public statesml_ParameterValue(
        ArrayList<statesml_IncomingParameter> statesml_incomingparameters    ) {
        this.statesml_incomingparameters = statesml_incomingparameters;
    }


    public statesml_FunctionCall getStatesml_functioncall() {
        return statesml_functioncall;
    }

    public void setStatesml_functioncall(statesml_FunctionCall statesml_functioncall) {
        this.statesml_functioncall = statesml_functioncall;
    }
    public List<statesml_IncomingParameter> getStatesml_incomingparameters() {
        return statesml_incomingparameters;
    }

    public void addStatesml_incomingparameter(Statesml_incomingparameter statesml_incomingparameter) {
        this.statesml_incomingparameters.add(statesml_incomingparameter);
    }

}