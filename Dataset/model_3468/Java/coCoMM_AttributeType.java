





import java.util.List;
import java.util.ArrayList;

public class coCoMM_AttributeType  {

    private String dataType;
    private String name;
    private String id;





    private coCoMM_FeatureAttribute cocomm_featureattribute;


    public coCoMM_AttributeType(
        String dataType,        String name,        String id    ) {
        this.dataType = dataType;
        this.name = name;
        this.id = id;
    }


    public String getDatatype() {
        return dataType;
    }

    public void setDatatype(String dataType) {
        this.dataType = dataType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public coCoMM_FeatureAttribute getCocomm_featureattribute() {
        return cocomm_featureattribute;
    }

    public void setCocomm_featureattribute(coCoMM_FeatureAttribute cocomm_featureattribute) {
        this.cocomm_featureattribute = cocomm_featureattribute;
    }

}