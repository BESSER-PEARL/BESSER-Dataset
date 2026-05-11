





import java.util.List;
import java.util.ArrayList;

public class qm_MeasurementResult extends Result {






    private qm_MeasurementMethod qm_measurementmethod;




    private qm_QualityModelResult qm_qualitymodelresult;


    public qm_MeasurementResult(
    ) {
        super(
        );
    }



    public qm_MeasurementMethod getQm_measurementmethod() {
        return qm_measurementmethod;
    }

    public void setQm_measurementmethod(qm_MeasurementMethod qm_measurementmethod) {
        this.qm_measurementmethod = qm_measurementmethod;
    }
    public qm_QualityModelResult getQm_qualitymodelresult() {
        return qm_qualitymodelresult;
    }

    public void setQm_qualitymodelresult(qm_QualityModelResult qm_qualitymodelresult) {
        this.qm_qualitymodelresult = qm_qualitymodelresult;
    }

}