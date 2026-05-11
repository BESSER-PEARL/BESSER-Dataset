





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwPower_HwPowerSupply extends HwComponent {

    private String capacity;
    private String suppliedPower;



    public MARTE_HwPower_HwPowerSupply(
        String capacity,        String suppliedPower    ) {
        super(
        );
        this.capacity = capacity;
        this.suppliedPower = suppliedPower;
    }


    public String getCapacity() {
        return capacity;
    }

    public void setCapacity(String capacity) {
        this.capacity = capacity;
    }
    public String getSuppliedpower() {
        return suppliedPower;
    }

    public void setSuppliedpower(String suppliedPower) {
        this.suppliedPower = suppliedPower;
    }


}