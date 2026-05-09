





import java.util.List;
import java.util.ArrayList;

public class QualityMetamodel_MetricProvider  {

    private String description;
    private String name;
    private String id;





    private QualityMetamodel_QualityModel qualitymetamodel_qualitymodel;


    public QualityMetamodel_MetricProvider(
        String description,        String name,        String id    ) {
        this.description = description;
        this.name = name;
        this.id = id;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
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

    public QualityMetamodel_QualityModel getQualitymetamodel_qualitymodel() {
        return qualitymetamodel_qualitymodel;
    }

    public void setQualitymetamodel_qualitymodel(QualityMetamodel_QualityModel qualitymetamodel_qualitymodel) {
        this.qualitymetamodel_qualitymodel = qualitymetamodel_qualitymodel;
    }

}