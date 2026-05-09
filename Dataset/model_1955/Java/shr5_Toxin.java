





import java.util.List;
import java.util.ArrayList;

public class shr5_Toxin extends Substance {

    private String effect;
    private int power;
    private int penetration;



    public shr5_Toxin(
        String effect,        int power,        int penetration    ) {
        super(
        );
        this.effect = effect;
        this.power = power;
        this.penetration = penetration;
    }


    public String getEffect() {
        return effect;
    }

    public void setEffect(String effect) {
        this.effect = effect;
    }
    public int getPower() {
        return power;
    }

    public void setPower(int power) {
        this.power = power;
    }
    public int getPenetration() {
        return penetration;
    }

    public void setPenetration(int penetration) {
        this.penetration = penetration;
    }


}