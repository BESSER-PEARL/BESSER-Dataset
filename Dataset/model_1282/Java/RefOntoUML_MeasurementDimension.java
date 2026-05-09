





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_MeasurementDimension extends MeasurementStructure {

    private String unitOfMeasure;



    public RefOntoUML_MeasurementDimension(
        String unitOfMeasure    ) {
        super(
        );
        this.unitOfMeasure = unitOfMeasure;
    }


    public String getUnitofmeasure() {
        return unitOfMeasure;
    }

    public void setUnitofmeasure(String unitOfMeasure) {
        this.unitOfMeasure = unitOfMeasure;
    }


}