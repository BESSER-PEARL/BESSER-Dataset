





import java.util.List;
import java.util.ArrayList;

public class standard_SIR extends SI {

    private float immunityLossRate;



    public standard_SIR(
        float immunityLossRate    ) {
        super(
        );
        this.immunityLossRate = immunityLossRate;
    }


    public float getImmunitylossrate() {
        return immunityLossRate;
    }

    public void setImmunitylossrate(float immunityLossRate) {
        this.immunityLossRate = immunityLossRate;
    }


}