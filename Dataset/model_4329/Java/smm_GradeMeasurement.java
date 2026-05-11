





import java.util.List;
import java.util.ArrayList;

public class smm_GradeMeasurement extends Measurement {

    private boolean isBaseSupplied;
    private String value;





    private smm_Operation smm_operation;




    private smm_GradeMeasurementRelationship smm_grademeasurementrelationship;


    public smm_GradeMeasurement(
        boolean isBaseSupplied,        String value    ) {
        super(
        );
        this.isBaseSupplied = isBaseSupplied;
        this.value = value;
    }


    public boolean getIsbasesupplied() {
        return isBaseSupplied;
    }

    public void setIsbasesupplied(boolean isBaseSupplied) {
        this.isBaseSupplied = isBaseSupplied;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public smm_Operation getSmm_operation() {
        return smm_operation;
    }

    public void setSmm_operation(smm_Operation smm_operation) {
        this.smm_operation = smm_operation;
    }
    public smm_GradeMeasurementRelationship getSmm_grademeasurementrelationship() {
        return smm_grademeasurementrelationship;
    }

    public void setSmm_grademeasurementrelationship(smm_GradeMeasurementRelationship smm_grademeasurementrelationship) {
        this.smm_grademeasurementrelationship = smm_grademeasurementrelationship;
    }

}