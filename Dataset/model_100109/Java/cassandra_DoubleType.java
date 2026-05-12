





import java.util.List;
import java.util.ArrayList;

public class cassandra_DoubleType extends DataType {

    private float value;



    public cassandra_DoubleType(
        float value    ) {
        super(
        );
        this.value = value;
    }


    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }


}