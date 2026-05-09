





import java.util.List;
import java.util.ArrayList;

public class cpsml_Variable  {

    private float Globalnv;
    private float value;



    public cpsml_Variable(
        float Globalnv,        float value    ) {
        this.Globalnv = Globalnv;
        this.value = value;
    }


    public float getGlobalnv() {
        return Globalnv;
    }

    public void setGlobalnv(float Globalnv) {
        this.Globalnv = Globalnv;
    }
    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }


}