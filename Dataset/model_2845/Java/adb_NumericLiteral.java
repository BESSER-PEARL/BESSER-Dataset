





import java.util.List;
import java.util.ArrayList;

public class adb_NumericLiteral extends Primary {

    private String value;



    public adb_NumericLiteral(
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