





import java.util.List;
import java.util.ArrayList;

public class QualityMetamodel_Operation  {

    private String body;
    private String name;





    private QualityMetamodel_AggregatedValue qualitymetamodel_aggregatedvalue;




    private List<QualityMetamodel_Value> qualitymetamodel_values;


    public QualityMetamodel_Operation(
        String body,        String name    ) {
        this.body = body;
        this.name = name;
        this.qualitymetamodel_values = new ArrayList<>();
    }

    public QualityMetamodel_Operation(
        String body,        String name        ArrayList<QualityMetamodel_Value> qualitymetamodel_values    ) {
        this.body = body;
        this.name = name;
        this.qualitymetamodel_values = qualitymetamodel_values;
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
    public List<QualityMetamodel_Value> getQualitymetamodel_values() {
        return qualitymetamodel_values;
    }

    public void addQualitymetamodel_value(Qualitymetamodel_value qualitymetamodel_value) {
        this.qualitymetamodel_values.add(qualitymetamodel_value);
    }

}