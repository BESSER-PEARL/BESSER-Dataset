





import java.util.List;
import java.util.ArrayList;

public class aml_SpeedFeature  {

    private float value;
    private String name;



    public aml_SpeedFeature(
        float value,        String name    ) {
        this.value = value;
        this.name = name;
    }


    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}