





import java.util.List;
import java.util.ArrayList;

public class avm_rf_RFPort extends DomainModelPort {

    private String Directionality;
    private String NominalImpedance;



    public avm_rf_RFPort(
        String Directionality,        String NominalImpedance    ) {
        super(
        );
        this.Directionality = Directionality;
        this.NominalImpedance = NominalImpedance;
    }


    public String getDirectionality() {
        return Directionality;
    }

    public void setDirectionality(String Directionality) {
        this.Directionality = Directionality;
    }
    public String getNominalimpedance() {
        return NominalImpedance;
    }

    public void setNominalimpedance(String NominalImpedance) {
        this.NominalImpedance = NominalImpedance;
    }


}