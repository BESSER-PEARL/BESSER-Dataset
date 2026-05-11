





import java.util.List;
import java.util.ArrayList;

public class dsml_web_BetweenValidator extends Validator {

    private int valueG;
    private int valueL;



    public dsml_web_BetweenValidator(
        int valueG,        int valueL    ) {
        super(
        );
        this.valueG = valueG;
        this.valueL = valueL;
    }


    public int getValueg() {
        return valueG;
    }

    public void setValueg(int valueG) {
        this.valueG = valueG;
    }
    public int getValuel() {
        return valueL;
    }

    public void setValuel(int valueL) {
        this.valueL = valueL;
    }


}