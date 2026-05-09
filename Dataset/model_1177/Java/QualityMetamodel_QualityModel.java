





import java.util.List;
import java.util.ArrayList;

public class QualityMetamodel_QualityModel extends Module {






    private List<QualityMetamodel_QualityAttribute> qualitymetamodel_qualityattributes;




    private List<QualityMetamodel_ValueType> qualitymetamodel_valuetypes;




    private List<QualityMetamodel_Value> qualitymetamodel_values;


    public QualityMetamodel_QualityModel(
    ) {
        super(
        );
        this.qualitymetamodel_qualityattributes = new ArrayList<>();
        this.qualitymetamodel_valuetypes = new ArrayList<>();
        this.qualitymetamodel_values = new ArrayList<>();
    }

    public QualityMetamodel_QualityModel(
        ArrayList<QualityMetamodel_QualityAttribute> qualitymetamodel_qualityattributes,        ArrayList<QualityMetamodel_ValueType> qualitymetamodel_valuetypes,        ArrayList<QualityMetamodel_Value> qualitymetamodel_values    ) {
        this.qualitymetamodel_qualityattributes = qualitymetamodel_qualityattributes;
        this.qualitymetamodel_valuetypes = qualitymetamodel_valuetypes;
        this.qualitymetamodel_values = qualitymetamodel_values;
    }


    public List<QualityMetamodel_QualityAttribute> getQualitymetamodel_qualityattributes() {
        return qualitymetamodel_qualityattributes;
    }

    public void addQualitymetamodel_qualityattribute(Qualitymetamodel_qualityattribute qualitymetamodel_qualityattribute) {
        this.qualitymetamodel_qualityattributes.add(qualitymetamodel_qualityattribute);
    }
    public List<QualityMetamodel_ValueType> getQualitymetamodel_valuetypes() {
        return qualitymetamodel_valuetypes;
    }

    public void addQualitymetamodel_valuetype(Qualitymetamodel_valuetype qualitymetamodel_valuetype) {
        this.qualitymetamodel_valuetypes.add(qualitymetamodel_valuetype);
    }
    public List<QualityMetamodel_Value> getQualitymetamodel_values() {
        return qualitymetamodel_values;
    }

    public void addQualitymetamodel_value(Qualitymetamodel_value qualitymetamodel_value) {
        this.qualitymetamodel_values.add(qualitymetamodel_value);
    }

}