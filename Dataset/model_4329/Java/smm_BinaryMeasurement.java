





import java.util.List;
import java.util.ArrayList;

public class smm_BinaryMeasurement extends DimensionalMeasurement {

    private String isBaseSupplied;





    private smm_Operation smm_operation;




    private smm_Base2MeasurementRelationship smm_base2measurementrelationship;




    private smm_Base1MeasurementRelationship smm_base1measurementrelationship;


    public smm_BinaryMeasurement(
        String isBaseSupplied    ) {
        super(
        );
        this.isBaseSupplied = isBaseSupplied;
    }


    public String getIsbasesupplied() {
        return isBaseSupplied;
    }

    public void setIsbasesupplied(String isBaseSupplied) {
        this.isBaseSupplied = isBaseSupplied;
    }

    public smm_Operation getSmm_operation() {
        return smm_operation;
    }

    public void setSmm_operation(smm_Operation smm_operation) {
        this.smm_operation = smm_operation;
    }
    public smm_Base2MeasurementRelationship getSmm_base2measurementrelationship() {
        return smm_base2measurementrelationship;
    }

    public void setSmm_base2measurementrelationship(smm_Base2MeasurementRelationship smm_base2measurementrelationship) {
        this.smm_base2measurementrelationship = smm_base2measurementrelationship;
    }
    public smm_Base1MeasurementRelationship getSmm_base1measurementrelationship() {
        return smm_base1measurementrelationship;
    }

    public void setSmm_base1measurementrelationship(smm_Base1MeasurementRelationship smm_base1measurementrelationship) {
        this.smm_base1measurementrelationship = smm_base1measurementrelationship;
    }

}