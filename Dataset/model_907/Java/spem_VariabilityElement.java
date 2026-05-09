





import java.util.List;
import java.util.ArrayList;

public class spem_VariabilityElement  {

    private String variabilityType;





    private spem_VariabilityElement spem_variabilityelement;


    public spem_VariabilityElement(
        String variabilityType    ) {
        this.variabilityType = variabilityType;
    }


    public String getVariabilitytype() {
        return variabilityType;
    }

    public void setVariabilitytype(String variabilityType) {
        this.variabilityType = variabilityType;
    }

    public spem_VariabilityElement getSpem_variabilityelement() {
        return spem_variabilityelement;
    }

    public void setSpem_variabilityelement(spem_VariabilityElement spem_variabilityelement) {
        this.spem_variabilityelement = spem_variabilityelement;
    }

}