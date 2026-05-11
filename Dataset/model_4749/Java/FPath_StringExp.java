





import java.util.List;
import java.util.ArrayList;

public class FPath_StringExp extends Expression {

    private String value;



    public FPath_StringExp(
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