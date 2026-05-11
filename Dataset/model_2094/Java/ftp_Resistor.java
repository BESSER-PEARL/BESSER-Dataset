





import java.util.List;
import java.util.ArrayList;

public class ftp_Resistor extends PrimitiveComponent {

    private float resistance;



    public ftp_Resistor(
        float resistance    ) {
        super(
        );
        this.resistance = resistance;
    }


    public float getResistance() {
        return resistance;
    }

    public void setResistance(float resistance) {
        this.resistance = resistance;
    }


}