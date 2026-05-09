





import java.util.List;
import java.util.ArrayList;

public class graphpattern_ValueBinding extends ParameterBinding {

    private String value;



    public graphpattern_ValueBinding(
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