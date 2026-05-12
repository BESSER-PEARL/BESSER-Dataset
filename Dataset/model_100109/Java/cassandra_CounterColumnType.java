





import java.util.List;
import java.util.ArrayList;

public class cassandra_CounterColumnType extends DataType {

    private String value;



    public cassandra_CounterColumnType(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}