





import java.util.List;
import java.util.ArrayList;

public class smm_DirectMeasure extends DimensionalMeasure {

    private String operation;



    public smm_DirectMeasure(
        String operation    ) {
        super(
        );
        this.operation = operation;
    }


    public String getOperation() {
        return operation;
    }

    public void setOperation(String operation) {
        this.operation = operation;
    }


}