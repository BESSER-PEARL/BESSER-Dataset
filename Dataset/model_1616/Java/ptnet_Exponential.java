





import java.util.List;
import java.util.ArrayList;

public class ptnet_Exponential extends Distribution {

    private float Rate;



    public ptnet_Exponential(
        float Rate    ) {
        super(
        );
        this.Rate = Rate;
    }


    public float getRate() {
        return Rate;
    }

    public void setRate(float Rate) {
        this.Rate = Rate;
    }


}