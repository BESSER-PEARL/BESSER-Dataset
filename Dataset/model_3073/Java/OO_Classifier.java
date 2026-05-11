





import java.util.List;
import java.util.ArrayList;

public class OO_Classifier extends PackageableElement {






    private OO_Feature oo_feature;




    private OO_Parameter oo_parameter;


    public OO_Classifier(
    ) {
        super(
        );
    }



    public OO_Feature getOo_feature() {
        return oo_feature;
    }

    public void setOo_feature(OO_Feature oo_feature) {
        this.oo_feature = oo_feature;
    }
    public OO_Parameter getOo_parameter() {
        return oo_parameter;
    }

    public void setOo_parameter(OO_Parameter oo_parameter) {
        this.oo_parameter = oo_parameter;
    }

}