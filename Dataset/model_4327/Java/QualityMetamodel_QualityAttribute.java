





import java.util.List;
import java.util.ArrayList;

public class QualityMetamodel_QualityAttribute  {

    private String name;





    private QualityMetamodel_QualityAttribute qualitymetamodel_qualityattribute;




    private QualityMetamodel_QualityModel qualitymetamodel_qualitymodel;


    public QualityMetamodel_QualityAttribute(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public QualityMetamodel_QualityAttribute getQualitymetamodel_qualityattribute() {
        return qualitymetamodel_qualityattribute;
    }

    public void setQualitymetamodel_qualityattribute(QualityMetamodel_QualityAttribute qualitymetamodel_qualityattribute) {
        this.qualitymetamodel_qualityattribute = qualitymetamodel_qualityattribute;
    }
    public QualityMetamodel_QualityModel getQualitymetamodel_qualitymodel() {
        return qualitymetamodel_qualitymodel;
    }

    public void setQualitymetamodel_qualitymodel(QualityMetamodel_QualityModel qualitymetamodel_qualitymodel) {
        this.qualitymetamodel_qualitymodel = qualitymetamodel_qualitymodel;
    }

}