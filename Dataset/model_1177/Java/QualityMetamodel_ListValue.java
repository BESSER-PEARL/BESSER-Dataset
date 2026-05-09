





import java.util.List;
import java.util.ArrayList;

public class QualityMetamodel_ListValue extends ValueType {






    private List<QualityMetamodel_ValueType> qualitymetamodel_valuetypes;


    public QualityMetamodel_ListValue(
    ) {
        super(
        );
        this.qualitymetamodel_valuetypes = new ArrayList<>();
    }

    public QualityMetamodel_ListValue(
        ArrayList<QualityMetamodel_ValueType> qualitymetamodel_valuetypes    ) {
        this.qualitymetamodel_valuetypes = qualitymetamodel_valuetypes;
    }


    public List<QualityMetamodel_ValueType> getQualitymetamodel_valuetypes() {
        return qualitymetamodel_valuetypes;
    }

    public void addQualitymetamodel_valuetype(Qualitymetamodel_valuetype qualitymetamodel_valuetype) {
        this.qualitymetamodel_valuetypes.add(qualitymetamodel_valuetype);
    }

}