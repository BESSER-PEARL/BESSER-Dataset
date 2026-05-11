





import java.util.List;
import java.util.ArrayList;

public class dsml_web_StringLengthValidator extends Validator {

    private int min;
    private int max;



    public dsml_web_StringLengthValidator(
        int min,        int max    ) {
        super(
        );
        this.min = min;
        this.max = max;
    }


    public int getMin() {
        return min;
    }

    public void setMin(int min) {
        this.min = min;
    }
    public int getMax() {
        return max;
    }

    public void setMax(int max) {
        this.max = max;
    }


}