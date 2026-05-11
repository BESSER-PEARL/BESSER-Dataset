





import java.util.List;
import java.util.ArrayList;

public class smm_Attribute extends SmmElement {

    private String value;
    private String tag;





    private smm_SmmElement smm_smmelement;




    private smm_SmmElement smm_smmelement;


    public smm_Attribute(
        String value,        String tag    ) {
        super(
        );
        this.value = value;
        this.tag = tag;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getTag() {
        return tag;
    }

    public void setTag(String tag) {
        this.tag = tag;
    }

    public smm_SmmElement getSmm_smmelement() {
        return smm_smmelement;
    }

    public void setSmm_smmelement(smm_SmmElement smm_smmelement) {
        this.smm_smmelement = smm_smmelement;
    }
    public smm_SmmElement getSmm_smmelement() {
        return smm_smmelement;
    }

    public void setSmm_smmelement(smm_SmmElement smm_smmelement) {
        this.smm_smmelement = smm_smmelement;
    }

}