





import java.util.List;
import java.util.ArrayList;

public class ptnet_Weibull extends Distribution {

    private float Beta;
    private float Alpha;



    public ptnet_Weibull(
        float Beta,        float Alpha    ) {
        super(
        );
        this.Beta = Beta;
        this.Alpha = Alpha;
    }


    public float getBeta() {
        return Beta;
    }

    public void setBeta(float Beta) {
        this.Beta = Beta;
    }
    public float getAlpha() {
        return Alpha;
    }

    public void setAlpha(float Alpha) {
        this.Alpha = Alpha;
    }


}