





import java.util.List;
import java.util.ArrayList;

public class smm_RescaledMeasureRelationship extends BaseMeasureRelationship {






    private smm_RescaledMeasure smm_rescaledmeasure;




    private smm_DimensionalMeasure smm_dimensionalmeasure;


    public smm_RescaledMeasureRelationship(
    ) {
        super(
        );
    }



    public smm_RescaledMeasure getSmm_rescaledmeasure() {
        return smm_rescaledmeasure;
    }

    public void setSmm_rescaledmeasure(smm_RescaledMeasure smm_rescaledmeasure) {
        this.smm_rescaledmeasure = smm_rescaledmeasure;
    }
    public smm_DimensionalMeasure getSmm_dimensionalmeasure() {
        return smm_dimensionalmeasure;
    }

    public void setSmm_dimensionalmeasure(smm_DimensionalMeasure smm_dimensionalmeasure) {
        this.smm_dimensionalmeasure = smm_dimensionalmeasure;
    }

}