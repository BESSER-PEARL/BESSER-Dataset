





import java.util.List;
import java.util.ArrayList;

public class afmmm_Attribute  {

    private String name;





    private afmmm_Feature afmmm_feature;


    public afmmm_Attribute(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public afmmm_Feature getAfmmm_feature() {
        return afmmm_feature;
    }

    public void setAfmmm_feature(afmmm_Feature afmmm_feature) {
        this.afmmm_feature = afmmm_feature;
    }

}