





import java.util.List;
import java.util.ArrayList;

public class EFM_Attribute extends FMElement {

    private String name;





    private EFM_Feature efm_feature;


    public EFM_Attribute(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public EFM_Feature getEfm_feature() {
        return efm_feature;
    }

    public void setEfm_feature(EFM_Feature efm_feature) {
        this.efm_feature = efm_feature;
    }

}