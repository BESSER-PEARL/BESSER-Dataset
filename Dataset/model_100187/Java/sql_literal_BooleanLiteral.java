





import java.util.List;
import java.util.ArrayList;

public class sql_literal_BooleanLiteral extends GeneralLiteral {

    private String value;



    public sql_literal_BooleanLiteral(
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