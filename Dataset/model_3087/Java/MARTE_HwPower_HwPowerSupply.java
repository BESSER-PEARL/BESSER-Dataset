





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwPower_HwPowerSupply extends HwComponent {






    private NFP_Power nfp_power;




    private NFP_Energy nfp_energy;


    public MARTE_HwPower_HwPowerSupply(
    ) {
        super(
        );
    }



    public NFP_Power getNfp_power() {
        return nfp_power;
    }

    public void setNfp_power(NFP_Power nfp_power) {
        this.nfp_power = nfp_power;
    }
    public NFP_Energy getNfp_energy() {
        return nfp_energy;
    }

    public void setNfp_energy(NFP_Energy nfp_energy) {
        this.nfp_energy = nfp_energy;
    }

}