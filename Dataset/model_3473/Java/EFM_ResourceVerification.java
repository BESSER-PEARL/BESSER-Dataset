





import java.util.List;
import java.util.ArrayList;

public class EFM_ResourceVerification extends FMConstraint {






    private EFM_Attribute efm_attribute;




    private List<EFM_Attribute> efm_attributes;


    public EFM_ResourceVerification(
    ) {
        super(
        );
        this.efm_attributes = new ArrayList<>();
    }

    public EFM_ResourceVerification(
        ArrayList<EFM_Attribute> efm_attributes    ) {
        this.efm_attributes = efm_attributes;
    }


    public EFM_Attribute getEfm_attribute() {
        return efm_attribute;
    }

    public void setEfm_attribute(EFM_Attribute efm_attribute) {
        this.efm_attribute = efm_attribute;
    }
    public List<EFM_Attribute> getEfm_attributes() {
        return efm_attributes;
    }

    public void addEfm_attribute(Efm_attribute efm_attribute) {
        this.efm_attributes.add(efm_attribute);
    }

}