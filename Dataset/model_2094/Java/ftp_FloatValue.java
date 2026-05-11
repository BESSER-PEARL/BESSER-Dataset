





import java.util.List;
import java.util.ArrayList;

public class ftp_FloatValue extends TypedPortValue {

    private float value;



    public ftp_FloatValue(
        float value    ) {
        super(
        );
        this.value = value;
    }


    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }


}