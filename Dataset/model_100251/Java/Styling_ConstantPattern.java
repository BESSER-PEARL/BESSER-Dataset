





import java.util.List;
import java.util.ArrayList;

public class Styling_ConstantPattern extends Pattern {

    private String value;



    public Styling_ConstantPattern(
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