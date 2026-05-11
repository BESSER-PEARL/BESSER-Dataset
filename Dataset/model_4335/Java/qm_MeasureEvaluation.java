





import java.util.List;
import java.util.ArrayList;

public class qm_MeasureEvaluation  {

    private String range;





    private qm_Function qm_function;




    private qm_NormalizationMeasure qm_normalizationmeasure;




    private qm_Measure qm_measure;


    public qm_MeasureEvaluation(
        String range    ) {
        this.range = range;
    }


    public String getRange() {
        return range;
    }

    public void setRange(String range) {
        this.range = range;
    }

    public qm_Function getQm_function() {
        return qm_function;
    }

    public void setQm_function(qm_Function qm_function) {
        this.qm_function = qm_function;
    }
    public qm_NormalizationMeasure getQm_normalizationmeasure() {
        return qm_normalizationmeasure;
    }

    public void setQm_normalizationmeasure(qm_NormalizationMeasure qm_normalizationmeasure) {
        this.qm_normalizationmeasure = qm_normalizationmeasure;
    }
    public qm_Measure getQm_measure() {
        return qm_measure;
    }

    public void setQm_measure(qm_Measure qm_measure) {
        this.qm_measure = qm_measure;
    }

}