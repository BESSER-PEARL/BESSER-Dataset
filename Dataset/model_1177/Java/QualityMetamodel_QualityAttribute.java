





import java.util.List;
import java.util.ArrayList;

public class QualityMetamodel_QualityAttribute extends VariableDeclaration {






    private List<QualityMetamodel_QualityAttribute> qualitymetamodel_qualityattributes;


    public QualityMetamodel_QualityAttribute(
    ) {
        super(
        );
        this.qualitymetamodel_qualityattributes = new ArrayList<>();
    }

    public QualityMetamodel_QualityAttribute(
        ArrayList<QualityMetamodel_QualityAttribute> qualitymetamodel_qualityattributes    ) {
        this.qualitymetamodel_qualityattributes = qualitymetamodel_qualityattributes;
    }


    public List<QualityMetamodel_QualityAttribute> getQualitymetamodel_qualityattributes() {
        return qualitymetamodel_qualityattributes;
    }

    public void addQualitymetamodel_qualityattribute(Qualitymetamodel_qualityattribute qualitymetamodel_qualityattribute) {
        this.qualitymetamodel_qualityattributes.add(qualitymetamodel_qualityattribute);
    }

}