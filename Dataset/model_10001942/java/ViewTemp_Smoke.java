





import java.util.List;
import java.util.ArrayList;

public class ViewTemp_Smoke  {

    private float SmokeValue;
    private float TempValue;



    public ViewTemp_Smoke(
        float SmokeValue,        float TempValue    ) {
        this.SmokeValue = SmokeValue;
        this.TempValue = TempValue;
    }


    public float getSmokevalue() {
        return SmokeValue;
    }

    public void setSmokevalue(float SmokeValue) {
        this.SmokeValue = SmokeValue;
    }
    public float getTempvalue() {
        return TempValue;
    }

    public void setTempvalue(float TempValue) {
        this.TempValue = TempValue;
    }


}