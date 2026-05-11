





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwPower_HwCoolingSupply extends HwComponent {

    private String coolingPower;



    public MARTE_HwPower_HwCoolingSupply(
        String coolingPower    ) {
        super(
        );
        this.coolingPower = coolingPower;
    }


    public String getCoolingpower() {
        return coolingPower;
    }

    public void setCoolingpower(String coolingPower) {
        this.coolingPower = coolingPower;
    }


}