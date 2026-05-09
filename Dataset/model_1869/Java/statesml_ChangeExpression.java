





import java.util.List;
import java.util.ArrayList;

public class statesml_ChangeExpression  {

    private boolean fulfilled;





    private statesml_ChangeEvent statesml_changeevent;




    private statesml_Function statesml_function;




    private List<statesml_IncomingParameter> statesml_incomingparameters;


    public statesml_ChangeExpression(
        boolean fulfilled    ) {
        this.fulfilled = fulfilled;
        this.statesml_incomingparameters = new ArrayList<>();
    }

    public statesml_ChangeExpression(
        boolean fulfilled        ArrayList<statesml_IncomingParameter> statesml_incomingparameters    ) {
        this.fulfilled = fulfilled;
        this.statesml_incomingparameters = statesml_incomingparameters;
    }

    public boolean getFulfilled() {
        return fulfilled;
    }

    public void setFulfilled(boolean fulfilled) {
        this.fulfilled = fulfilled;
    }

    public statesml_ChangeEvent getStatesml_changeevent() {
        return statesml_changeevent;
    }

    public void setStatesml_changeevent(statesml_ChangeEvent statesml_changeevent) {
        this.statesml_changeevent = statesml_changeevent;
    }
    public statesml_Function getStatesml_function() {
        return statesml_function;
    }

    public void setStatesml_function(statesml_Function statesml_function) {
        this.statesml_function = statesml_function;
    }
    public List<statesml_IncomingParameter> getStatesml_incomingparameters() {
        return statesml_incomingparameters;
    }

    public void addStatesml_incomingparameter(Statesml_incomingparameter statesml_incomingparameter) {
        this.statesml_incomingparameters.add(statesml_incomingparameter);
    }

}