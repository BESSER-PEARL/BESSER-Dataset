





import java.util.List;
import java.util.ArrayList;

public class DiagonosticModel_Action extends TestStep {

    private float wait;
    private String valueTo;
    private String value;



    public DiagonosticModel_Action(
        float wait,        String valueTo,        String value    ) {
        super(
        );
        this.wait = wait;
        this.valueTo = valueTo;
        this.value = value;
    }


    public float getWait() {
        return wait;
    }

    public void setWait(float wait) {
        this.wait = wait;
    }
    public String getValueto() {
        return valueTo;
    }

    public void setValueto(String valueTo) {
        this.valueTo = valueTo;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}