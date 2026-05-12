





import java.util.List;
import java.util.ArrayList;

public class prozessHeizen  {

    private String temperatur_ist;
    private String attribute;





    private backofen backofen;


    public prozessHeizen(
        String temperatur_ist,        String attribute    ) {
        this.temperatur_ist = temperatur_ist;
        this.attribute = attribute;
    }


    public String getTemperatur_ist() {
        return temperatur_ist;
    }

    public void setTemperatur_ist(String temperatur_ist) {
        this.temperatur_ist = temperatur_ist;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }

    public backofen getBackofen() {
        return backofen;
    }

    public void setBackofen(backofen backofen) {
        this.backofen = backofen;
    }

}