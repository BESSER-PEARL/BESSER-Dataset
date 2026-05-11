





import java.util.List;
import java.util.ArrayList;

public class trnetvisual_ExternalCalculationCall extends Calculation {

    private String qualifiedName;
    private String id;





    private trnetvisual_ExternalCalculationCallParameter trnetvisual_externalcalculationcallparameter;




    private List<trnetvisual_ExternalCalculationCallParameter> trnetvisual_externalcalculationcallparameters;


    public trnetvisual_ExternalCalculationCall(
        String qualifiedName,        String id    ) {
        super(
        );
        this.qualifiedName = qualifiedName;
        this.id = id;
        this.trnetvisual_externalcalculationcallparameters = new ArrayList<>();
    }

    public trnetvisual_ExternalCalculationCall(
        String qualifiedName,        String id        ArrayList<trnetvisual_ExternalCalculationCallParameter> trnetvisual_externalcalculationcallparameters    ) {
        this.qualifiedName = qualifiedName;
        this.id = id;
        this.trnetvisual_externalcalculationcallparameters = trnetvisual_externalcalculationcallparameters;
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

    public trnetvisual_ExternalCalculationCallParameter getTrnetvisual_externalcalculationcallparameter() {
        return trnetvisual_externalcalculationcallparameter;
    }

    public void setTrnetvisual_externalcalculationcallparameter(trnetvisual_ExternalCalculationCallParameter trnetvisual_externalcalculationcallparameter) {
        this.trnetvisual_externalcalculationcallparameter = trnetvisual_externalcalculationcallparameter;
    }
    public List<trnetvisual_ExternalCalculationCallParameter> getTrnetvisual_externalcalculationcallparameters() {
        return trnetvisual_externalcalculationcallparameters;
    }

    public void addTrnetvisual_externalcalculationcallparameter(Trnetvisual_externalcalculationcallparameter trnetvisual_externalcalculationcallparameter) {
        this.trnetvisual_externalcalculationcallparameters.add(trnetvisual_externalcalculationcallparameter);
    }

}