





import java.util.List;
import java.util.ArrayList;

public class spem_WorkProductDefinition extends MethodContentElement {

    private String impactOfNotHaving;
    private String reasonForNotNeeding;





    private spem_WorkDefinitionParameter spem_workdefinitionparameter;


    public spem_WorkProductDefinition(
        String impactOfNotHaving,        String reasonForNotNeeding    ) {
        super(
        );
        this.impactOfNotHaving = impactOfNotHaving;
        this.reasonForNotNeeding = reasonForNotNeeding;
    }


    public String getImpactofnothaving() {
        return impactOfNotHaving;
    }

    public void setImpactofnothaving(String impactOfNotHaving) {
        this.impactOfNotHaving = impactOfNotHaving;
    }
    public String getReasonfornotneeding() {
        return reasonForNotNeeding;
    }

    public void setReasonfornotneeding(String reasonForNotNeeding) {
        this.reasonForNotNeeding = reasonForNotNeeding;
    }

    public spem_WorkDefinitionParameter getSpem_workdefinitionparameter() {
        return spem_workdefinitionparameter;
    }

    public void setSpem_workdefinitionparameter(spem_WorkDefinitionParameter spem_workdefinitionparameter) {
        this.spem_workdefinitionparameter = spem_workdefinitionparameter;
    }

}