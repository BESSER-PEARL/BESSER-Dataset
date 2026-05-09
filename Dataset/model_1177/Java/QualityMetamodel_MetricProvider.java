





import java.util.List;
import java.util.ArrayList;

public class QualityMetamodel_MetricProvider  {

    private String name;
    private String id;
    private String description;





    private QualityMetamodel_SingleValue qualitymetamodel_singlevalue;




    private QualityMetamodel_QualityModel qualitymetamodel_qualitymodel;


    public QualityMetamodel_MetricProvider(
        String name,        String id,        String description    ) {
        this.name = name;
        this.id = id;
        this.description = description;
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
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public QualityMetamodel_SingleValue getQualitymetamodel_singlevalue() {
        return qualitymetamodel_singlevalue;
    }

    public void setQualitymetamodel_singlevalue(QualityMetamodel_SingleValue qualitymetamodel_singlevalue) {
        this.qualitymetamodel_singlevalue = qualitymetamodel_singlevalue;
    }
    public QualityMetamodel_QualityModel getQualitymetamodel_qualitymodel() {
        return qualitymetamodel_qualitymodel;
    }

    public void setQualitymetamodel_qualitymodel(QualityMetamodel_QualityModel qualitymetamodel_qualitymodel) {
        this.qualitymetamodel_qualitymodel = qualitymetamodel_qualitymodel;
    }

}