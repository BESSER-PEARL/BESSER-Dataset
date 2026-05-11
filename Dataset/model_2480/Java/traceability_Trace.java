





import java.util.List;
import java.util.ArrayList;

public class traceability_Trace  {

    private String ruleDescriptorId;





    private traceability_Traceability traceability_traceability;


    public traceability_Trace(
        String ruleDescriptorId    ) {
        this.ruleDescriptorId = ruleDescriptorId;
    }


    public String getRuledescriptorid() {
        return ruleDescriptorId;
    }

    public void setRuledescriptorid(String ruleDescriptorId) {
        this.ruleDescriptorId = ruleDescriptorId;
    }

    public traceability_Traceability getTraceability_traceability() {
        return traceability_traceability;
    }

    public void setTraceability_traceability(traceability_Traceability traceability_traceability) {
        this.traceability_traceability = traceability_traceability;
    }

}