





import java.util.List;
import java.util.ArrayList;

public class QualityMetamodel_Operation  {

    private String body;
    private String name;





    private QualityMetamodel_AggregatedValue qualitymetamodel_aggregatedvalue;


    public QualityMetamodel_Operation(
        String body,        String name    ) {
        this.body = body;
        this.name = name;
    }


    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public QualityMetamodel_AggregatedValue getQualitymetamodel_aggregatedvalue() {
        return qualitymetamodel_aggregatedvalue;
    }

    public void setQualitymetamodel_aggregatedvalue(QualityMetamodel_AggregatedValue qualitymetamodel_aggregatedvalue) {
        this.qualitymetamodel_aggregatedvalue = qualitymetamodel_aggregatedvalue;
    }

}