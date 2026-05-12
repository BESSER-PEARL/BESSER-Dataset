





import java.util.List;
import java.util.ArrayList;

public class cassandra_BooleanType extends DataType {

    private boolean value;



    public cassandra_BooleanType(
        boolean value    ) {
        super(
        );
        this.value = value;
    }


    public boolean getValue() {
        return value;
    }

    public void setValue(boolean value) {
        this.value = value;
    }


}