





import java.util.List;
import java.util.ArrayList;

public class qm_MeasureRanking extends MeasureEvaluation, Ranking {






    private qm_WeightedSumMultiMeasureEvaluation qm_weightedsummultimeasureevaluation;


    public qm_MeasureRanking(
    ) {
        super(
        );
    }



    public qm_WeightedSumMultiMeasureEvaluation getQm_weightedsummultimeasureevaluation() {
        return qm_weightedsummultimeasureevaluation;
    }

    public void setQm_weightedsummultimeasureevaluation(qm_WeightedSumMultiMeasureEvaluation qm_weightedsummultimeasureevaluation) {
        this.qm_weightedsummultimeasureevaluation = qm_weightedsummultimeasureevaluation;
    }

}