





import java.util.List;
import java.util.ArrayList;

public class FPath_NumberExp extends Expression {

    private String value;



    public FPath_NumberExp(
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