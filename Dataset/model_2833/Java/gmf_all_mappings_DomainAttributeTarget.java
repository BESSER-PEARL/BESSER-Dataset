





import java.util.List;
import java.util.ArrayList;

public class gmf_all_mappings_DomainAttributeTarget extends Auditable {

    private boolean nullAsError;





    private mappings_gmf_all_EAttribute mappings_gmf_all_eattribute;


    public gmf_all_mappings_DomainAttributeTarget(
        boolean nullAsError    ) {
        super(
        );
        this.nullAsError = nullAsError;
    }


    public boolean getNullaserror() {
        return nullAsError;
    }

    public void setNullaserror(boolean nullAsError) {
        this.nullAsError = nullAsError;
    }

    public mappings_gmf_all_EAttribute getMappings_gmf_all_eattribute() {
        return mappings_gmf_all_eattribute;
    }

    public void setMappings_gmf_all_eattribute(mappings_gmf_all_EAttribute mappings_gmf_all_eattribute) {
        this.mappings_gmf_all_eattribute = mappings_gmf_all_eattribute;
    }

}