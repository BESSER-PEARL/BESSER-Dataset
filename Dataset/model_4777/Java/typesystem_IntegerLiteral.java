





import java.util.List;
import java.util.ArrayList;

public class typesystem_IntegerLiteral extends NumericLiteral {

    private String data;
    private String value;



    public typesystem_IntegerLiteral(
        String data,        String value    ) {
        super(
        );
        this.data = data;
        this.value = value;
    }


    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}