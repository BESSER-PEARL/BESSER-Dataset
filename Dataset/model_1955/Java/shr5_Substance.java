





import java.util.List;
import java.util.ArrayList;

public class shr5_Substance extends Quelle, Beschreibbar, GeldWert, Menge {

    private String speed;
    private String vector;



    public shr5_Substance(
        String speed,        String vector    ) {
        super(
        );
        this.speed = speed;
        this.vector = vector;
    }


    public String getSpeed() {
        return speed;
    }

    public void setSpeed(String speed) {
        this.speed = speed;
    }
    public String getVector() {
        return vector;
    }

    public void setVector(String vector) {
        this.vector = vector;
    }


}