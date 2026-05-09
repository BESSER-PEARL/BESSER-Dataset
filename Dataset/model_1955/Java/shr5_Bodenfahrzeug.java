





import java.util.List;
import java.util.ArrayList;

public class shr5_Bodenfahrzeug extends PassagierFahrzeug {

    private int geschwindigkeitGelaende;
    private int handlingGelaende;



    public shr5_Bodenfahrzeug(
        int geschwindigkeitGelaende,        int handlingGelaende    ) {
        super(
        );
        this.geschwindigkeitGelaende = geschwindigkeitGelaende;
        this.handlingGelaende = handlingGelaende;
    }


    public int getGeschwindigkeitgelaende() {
        return geschwindigkeitGelaende;
    }

    public void setGeschwindigkeitgelaende(int geschwindigkeitGelaende) {
        this.geschwindigkeitGelaende = geschwindigkeitGelaende;
    }
    public int getHandlinggelaende() {
        return handlingGelaende;
    }

    public void setHandlinggelaende(int handlingGelaende) {
        this.handlingGelaende = handlingGelaende;
    }


}