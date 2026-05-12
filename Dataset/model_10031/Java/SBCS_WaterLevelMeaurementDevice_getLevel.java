





import java.util.List;
import java.util.ArrayList;

public class SBCS_WaterLevelMeaurementDevice_getLevel extends Transition {

    private float ret;



    public SBCS_WaterLevelMeaurementDevice_getLevel(
        float ret    ) {
        super(
        );
        this.ret = ret;
    }


    public float getRet() {
        return ret;
    }

    public void setRet(float ret) {
        this.ret = ret;
    }


}