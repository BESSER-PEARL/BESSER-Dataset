





import java.util.List;
import java.util.ArrayList;

public class qualitymodel_LeafAttribute extends Attribute {

    private float normalizationMin;
    private String normalizationKind;
    private int numSamples;
    private float normalizationMax;
    private String operator;





    private qualitymodel_Metric qualitymodel_metric;


    public qualitymodel_LeafAttribute(
        float normalizationMin,        String normalizationKind,        int numSamples,        float normalizationMax,        String operator    ) {
        super(
        );
        this.normalizationMin = normalizationMin;
        this.normalizationKind = normalizationKind;
        this.numSamples = numSamples;
        this.normalizationMax = normalizationMax;
        this.operator = operator;
    }


    public float getNormalizationmin() {
        return normalizationMin;
    }

    public void setNormalizationmin(float normalizationMin) {
        this.normalizationMin = normalizationMin;
    }
    public String getNormalizationkind() {
        return normalizationKind;
    }

    public void setNormalizationkind(String normalizationKind) {
        this.normalizationKind = normalizationKind;
    }
    public int getNumsamples() {
        return numSamples;
    }

    public void setNumsamples(int numSamples) {
        this.numSamples = numSamples;
    }
    public float getNormalizationmax() {
        return normalizationMax;
    }

    public void setNormalizationmax(float normalizationMax) {
        this.normalizationMax = normalizationMax;
    }
    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public qualitymodel_Metric getQualitymodel_metric() {
        return qualitymodel_metric;
    }

    public void setQualitymodel_metric(qualitymodel_Metric qualitymodel_metric) {
        this.qualitymodel_metric = qualitymodel_metric;
    }

}