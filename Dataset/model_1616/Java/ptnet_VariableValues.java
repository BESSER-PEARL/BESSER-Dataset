





import java.util.List;
import java.util.ArrayList;

public class ptnet_VariableValues  {

    private float values;





    private ptnet_Study ptnet_study;


    public ptnet_VariableValues(
        float values    ) {
        this.values = values;
    }


    public float getValues() {
        return values;
    }

    public void setValues(float values) {
        this.values = values;
    }

    public ptnet_Study getPtnet_study() {
        return ptnet_study;
    }

    public void setPtnet_study(ptnet_Study ptnet_study) {
        this.ptnet_study = ptnet_study;
    }

}