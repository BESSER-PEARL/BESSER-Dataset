





import java.util.List;
import java.util.ArrayList;

public class rapidml_PropertyRealization extends ConstrainableType {

    private String cardinality;





    private rapidml_ObjectRealization rapidml_objectrealization;




    private rapidml_ObjectRealization rapidml_objectrealization;




    private rapidml_Feature rapidml_feature;


    public rapidml_PropertyRealization(
        String cardinality    ) {
        super(
        );
        this.cardinality = cardinality;
    }


    public String getCardinality() {
        return cardinality;
    }

    public void setCardinality(String cardinality) {
        this.cardinality = cardinality;
    }

    public rapidml_ObjectRealization getRapidml_objectrealization() {
        return rapidml_objectrealization;
    }

    public void setRapidml_objectrealization(rapidml_ObjectRealization rapidml_objectrealization) {
        this.rapidml_objectrealization = rapidml_objectrealization;
    }
    public rapidml_ObjectRealization getRapidml_objectrealization() {
        return rapidml_objectrealization;
    }

    public void setRapidml_objectrealization(rapidml_ObjectRealization rapidml_objectrealization) {
        this.rapidml_objectrealization = rapidml_objectrealization;
    }
    public rapidml_Feature getRapidml_feature() {
        return rapidml_feature;
    }

    public void setRapidml_feature(rapidml_Feature rapidml_feature) {
        this.rapidml_feature = rapidml_feature;
    }

}