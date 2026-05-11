





import java.util.List;
import java.util.ArrayList;

public class oml_Classifier extends PackageableElement {






    private oml_Feature oml_feature;




    private oml_Parameter oml_parameter;


    public oml_Classifier(
    ) {
        super(
        );
    }



    public oml_Feature getOml_feature() {
        return oml_feature;
    }

    public void setOml_feature(oml_Feature oml_feature) {
        this.oml_feature = oml_feature;
    }
    public oml_Parameter getOml_parameter() {
        return oml_parameter;
    }

    public void setOml_parameter(oml_Parameter oml_parameter) {
        this.oml_parameter = oml_parameter;
    }

}