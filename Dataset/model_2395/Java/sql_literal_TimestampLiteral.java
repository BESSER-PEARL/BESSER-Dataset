





import java.util.List;
import java.util.ArrayList;

public class sql_literal_TimestampLiteral extends DatetimeLiteral {

    private String value;



    public sql_literal_TimestampLiteral(
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