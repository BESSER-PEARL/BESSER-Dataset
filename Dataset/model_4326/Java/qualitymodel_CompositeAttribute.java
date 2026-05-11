





import java.util.List;
import java.util.ArrayList;

public class qualitymodel_CompositeAttribute extends Attribute {

    private String operator;





    private List<qualitymodel_Attribute> qualitymodel_attributes;


    public qualitymodel_CompositeAttribute(
        String operator    ) {
        super(
        );
        this.operator = operator;
        this.qualitymodel_attributes = new ArrayList<>();
    }

    public qualitymodel_CompositeAttribute(
        String operator        ArrayList<qualitymodel_Attribute> qualitymodel_attributes    ) {
        this.operator = operator;
        this.qualitymodel_attributes = qualitymodel_attributes;
    }

    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public List<qualitymodel_Attribute> getQualitymodel_attributes() {
        return qualitymodel_attributes;
    }

    public void addQualitymodel_attribute(Qualitymodel_attribute qualitymodel_attribute) {
        this.qualitymodel_attributes.add(qualitymodel_attribute);
    }

}