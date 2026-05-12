





import java.util.List;
import java.util.ArrayList;

public class prozessBand  {

    private String geschwindigkeit_ist;





    private backofen backofen;


    public prozessBand(
        String geschwindigkeit_ist    ) {
        this.geschwindigkeit_ist = geschwindigkeit_ist;
    }


    public String getGeschwindigkeit_ist() {
        return geschwindigkeit_ist;
    }

    public void setGeschwindigkeit_ist(String geschwindigkeit_ist) {
        this.geschwindigkeit_ist = geschwindigkeit_ist;
    }

    public backofen getBackofen() {
        return backofen;
    }

    public void setBackofen(backofen backofen) {
        this.backofen = backofen;
    }

}