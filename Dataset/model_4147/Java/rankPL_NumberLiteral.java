





import java.util.List;
import java.util.ArrayList;

public class rankPL_NumberLiteral extends Expression {

    private String value;



    public rankPL_NumberLiteral(
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