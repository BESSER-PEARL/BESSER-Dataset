





import java.util.List;
import java.util.ArrayList;

public class smm_RankingMeasurement extends DimensionalMeasurement {

    private String isBaseSupplied;





    private smm_Operation smm_operation;


    public smm_RankingMeasurement(
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

}