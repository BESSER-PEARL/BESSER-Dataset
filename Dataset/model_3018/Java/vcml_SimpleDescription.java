





import java.util.List;
import java.util.ArrayList;

public class vcml_SimpleDescription extends Description {

    private String value;



    public vcml_SimpleDescription(
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