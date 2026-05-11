





import java.util.List;
import java.util.ArrayList;

public class SPL_StringConstant extends Constant {

    private String value;



    public SPL_StringConstant(
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