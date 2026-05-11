





import java.util.List;
import java.util.ArrayList;

public class trnetvisual_Parameter  {






    private List<trnetvisual_ExternalActionCallParameter> trnetvisual_externalactioncallparameters;




    private List<trnetvisual_ExternalAttributeCalculationCallParameter> trnetvisual_externalattributecalculationcallparameters;




    private trnetvisual_ExternalCalculationCallParameter trnetvisual_externalcalculationcallparameter;




    private trnetvisual_ExternalConditionCallParameter trnetvisual_externalconditioncallparameter;




    private trnetvisual_ExternalActionCallParameter trnetvisual_externalactioncallparameter;




    private List<trnetvisual_ExternalCalculationCallParameter> trnetvisual_externalcalculationcallparameters;




    private trnetvisual_ExternalAttributeCalculationCallParameter trnetvisual_externalattributecalculationcallparameter;




    private List<trnetvisual_ExternalConditionCallParameter> trnetvisual_externalconditioncallparameters;


    public trnetvisual_Parameter(
    ) {
        this.trnetvisual_externalactioncallparameters = new ArrayList<>();
        this.trnetvisual_externalattributecalculationcallparameters = new ArrayList<>();
        this.trnetvisual_externalcalculationcallparameters = new ArrayList<>();
        this.trnetvisual_externalconditioncallparameters = new ArrayList<>();
    }

    public trnetvisual_Parameter(
        ArrayList<trnetvisual_ExternalActionCallParameter> trnetvisual_externalactioncallparameters,        ArrayList<trnetvisual_ExternalAttributeCalculationCallParameter> trnetvisual_externalattributecalculationcallparameters,        ArrayList<trnetvisual_ExternalCalculationCallParameter> trnetvisual_externalcalculationcallparameters,        ArrayList<trnetvisual_ExternalConditionCallParameter> trnetvisual_externalconditioncallparameters    ) {
        this.trnetvisual_externalactioncallparameters = trnetvisual_externalactioncallparameters;
        this.trnetvisual_externalattributecalculationcallparameters = trnetvisual_externalattributecalculationcallparameters;
        this.trnetvisual_externalcalculationcallparameters = trnetvisual_externalcalculationcallparameters;
        this.trnetvisual_externalconditioncallparameters = trnetvisual_externalconditioncallparameters;
    }


    public List<trnetvisual_ExternalActionCallParameter> getTrnetvisual_externalactioncallparameters() {
        return trnetvisual_externalactioncallparameters;
    }

    public void addTrnetvisual_externalactioncallparameter(Trnetvisual_externalactioncallparameter trnetvisual_externalactioncallparameter) {
        this.trnetvisual_externalactioncallparameters.add(trnetvisual_externalactioncallparameter);
    }
    public List<trnetvisual_ExternalAttributeCalculationCallParameter> getTrnetvisual_externalattributecalculationcallparameters() {
        return trnetvisual_externalattributecalculationcallparameters;
    }

    public void addTrnetvisual_externalattributecalculationcallparameter(Trnetvisual_externalattributecalculationcallparameter trnetvisual_externalattributecalculationcallparameter) {
        this.trnetvisual_externalattributecalculationcallparameters.add(trnetvisual_externalattributecalculationcallparameter);
    }
    public trnetvisual_ExternalCalculationCallParameter getTrnetvisual_externalcalculationcallparameter() {
        return trnetvisual_externalcalculationcallparameter;
    }

    public void setTrnetvisual_externalcalculationcallparameter(trnetvisual_ExternalCalculationCallParameter trnetvisual_externalcalculationcallparameter) {
        this.trnetvisual_externalcalculationcallparameter = trnetvisual_externalcalculationcallparameter;
    }
    public trnetvisual_ExternalConditionCallParameter getTrnetvisual_externalconditioncallparameter() {
        return trnetvisual_externalconditioncallparameter;
    }

    public void setTrnetvisual_externalconditioncallparameter(trnetvisual_ExternalConditionCallParameter trnetvisual_externalconditioncallparameter) {
        this.trnetvisual_externalconditioncallparameter = trnetvisual_externalconditioncallparameter;
    }
    public trnetvisual_ExternalActionCallParameter getTrnetvisual_externalactioncallparameter() {
        return trnetvisual_externalactioncallparameter;
    }

    public void setTrnetvisual_externalactioncallparameter(trnetvisual_ExternalActionCallParameter trnetvisual_externalactioncallparameter) {
        this.trnetvisual_externalactioncallparameter = trnetvisual_externalactioncallparameter;
    }
    public List<trnetvisual_ExternalCalculationCallParameter> getTrnetvisual_externalcalculationcallparameters() {
        return trnetvisual_externalcalculationcallparameters;
    }

    public void addTrnetvisual_externalcalculationcallparameter(Trnetvisual_externalcalculationcallparameter trnetvisual_externalcalculationcallparameter) {
        this.trnetvisual_externalcalculationcallparameters.add(trnetvisual_externalcalculationcallparameter);
    }
    public trnetvisual_ExternalAttributeCalculationCallParameter getTrnetvisual_externalattributecalculationcallparameter() {
        return trnetvisual_externalattributecalculationcallparameter;
    }

    public void setTrnetvisual_externalattributecalculationcallparameter(trnetvisual_ExternalAttributeCalculationCallParameter trnetvisual_externalattributecalculationcallparameter) {
        this.trnetvisual_externalattributecalculationcallparameter = trnetvisual_externalattributecalculationcallparameter;
    }
    public List<trnetvisual_ExternalConditionCallParameter> getTrnetvisual_externalconditioncallparameters() {
        return trnetvisual_externalconditioncallparameters;
    }

    public void addTrnetvisual_externalconditioncallparameter(Trnetvisual_externalconditioncallparameter trnetvisual_externalconditioncallparameter) {
        this.trnetvisual_externalconditioncallparameters.add(trnetvisual_externalconditioncallparameter);
    }

}