





import java.util.List;
import java.util.ArrayList;

public class cassandra_FloatType extends DataType {

    private float value;



    public cassandra_FloatType(
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