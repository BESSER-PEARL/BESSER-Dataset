





import java.util.List;
import java.util.ArrayList;

public class QualityMetamodel_QualityAttribute extends VariableDeclaration {






    private QualityMetamodel_QualityModel qualitymetamodel_qualitymodel;




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


    public QualityMetamodel_QualityModel getQualitymetamodel_qualitymodel() {
        return qualitymetamodel_qualitymodel;
    }

    public void setQualitymetamodel_qualitymodel(QualityMetamodel_QualityModel qualitymetamodel_qualitymodel) {
        this.qualitymetamodel_qualitymodel = qualitymetamodel_qualitymodel;
    }
    public List<QualityMetamodel_QualityAttribute> getQualitymetamodel_qualityattributes() {
        return qualitymetamodel_qualityattributes;
    }

    public void addQualitymetamodel_qualityattribute(Qualitymetamodel_qualityattribute qualitymetamodel_qualityattribute) {
        this.qualitymetamodel_qualityattributes.add(qualitymetamodel_qualityattribute);
    }

}