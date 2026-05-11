





import java.util.List;
import java.util.ArrayList;

public class dsml_web_GreaterThanValidator extends Validator {

    private int value;



    public dsml_web_GreaterThanValidator(
        int value    ) {
        super(
        );
        this.value = value;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }


}