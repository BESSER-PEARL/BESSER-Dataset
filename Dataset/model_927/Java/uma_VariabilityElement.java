





import java.util.List;
import java.util.ArrayList;

public class uma_VariabilityElement extends MethodElement {

    private String variabilityType;





    private uma_VariabilityElement uma_variabilityelement;


    public uma_VariabilityElement(
        String variabilityType    ) {
        super(
        );
        this.variabilityType = variabilityType;
    }


    public String getVariabilitytype() {
        return variabilityType;
    }

    public void setVariabilitytype(String variabilityType) {
        this.variabilityType = variabilityType;
    }

    public uma_VariabilityElement getUma_variabilityelement() {
        return uma_variabilityelement;
    }

    public void setUma_variabilityelement(uma_VariabilityElement uma_variabilityelement) {
        this.uma_variabilityelement = uma_variabilityelement;
    }

}