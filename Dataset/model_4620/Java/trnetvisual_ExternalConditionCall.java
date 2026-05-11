





import java.util.List;
import java.util.ArrayList;

public class trnetvisual_ExternalConditionCall extends ApplicationCondition {

    private String qualifiedName;
    private String id;





    private trnetvisual_ExternalConditionCallParameter trnetvisual_externalconditioncallparameter;




    private List<trnetvisual_ExternalConditionCallParameter> trnetvisual_externalconditioncallparameters;


    public trnetvisual_ExternalConditionCall(
        String qualifiedName,        String id    ) {
        super(
        );
        this.qualifiedName = qualifiedName;
        this.id = id;
        this.trnetvisual_externalconditioncallparameters = new ArrayList<>();
    }

    public trnetvisual_ExternalConditionCall(
        String qualifiedName,        String id        ArrayList<trnetvisual_ExternalConditionCallParameter> trnetvisual_externalconditioncallparameters    ) {
        this.qualifiedName = qualifiedName;
        this.id = id;
        this.trnetvisual_externalconditioncallparameters = trnetvisual_externalconditioncallparameters;
    }

    public String getQualifiedname() {
        return qualifiedName;
    }

    public void setQualifiedname(String qualifiedName) {
        this.qualifiedName = qualifiedName;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public trnetvisual_ExternalConditionCallParameter getTrnetvisual_externalconditioncallparameter() {
        return trnetvisual_externalconditioncallparameter;
    }

    public void setTrnetvisual_externalconditioncallparameter(trnetvisual_ExternalConditionCallParameter trnetvisual_externalconditioncallparameter) {
        this.trnetvisual_externalconditioncallparameter = trnetvisual_externalconditioncallparameter;
    }
    public List<trnetvisual_ExternalConditionCallParameter> getTrnetvisual_externalconditioncallparameters() {
        return trnetvisual_externalconditioncallparameters;
    }

    public void addTrnetvisual_externalconditioncallparameter(Trnetvisual_externalconditioncallparameter trnetvisual_externalconditioncallparameter) {
        this.trnetvisual_externalconditioncallparameters.add(trnetvisual_externalconditioncallparameter);
    }

}