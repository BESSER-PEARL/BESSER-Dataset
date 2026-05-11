





import java.util.List;
import java.util.ArrayList;

public class assignment6_model_IntegerValueDependency extends UnaryDependency {

    private int value;





    private assignment6_model_IntegerFeature assignment6_model_integerfeature;


    public assignment6_model_IntegerValueDependency(
        int value    ) {
        super(
        );
        this.value = value;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public assignment6_model_IntegerFeature getAssignment6_model_integerfeature() {
        return assignment6_model_integerfeature;
    }

    public void setAssignment6_model_integerfeature(assignment6_model_IntegerFeature assignment6_model_integerfeature) {
        this.assignment6_model_integerfeature = assignment6_model_integerfeature;
    }

}