





import java.util.List;
import java.util.ArrayList;

public class cassandra_BytesType extends DataType {

    private String value;



    public cassandra_BytesType(
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