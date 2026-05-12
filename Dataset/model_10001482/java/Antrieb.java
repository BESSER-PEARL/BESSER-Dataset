





import java.util.List;
import java.util.ArrayList;

public class Antrieb  {

    private String aNTRIEBSART;





    private TurboliftSchacht turboliftschacht;


    public Antrieb(
        String aNTRIEBSART    ) {
        this.aNTRIEBSART = aNTRIEBSART;
    }


    public String getAntriebsart() {
        return aNTRIEBSART;
    }

    public void setAntriebsart(String aNTRIEBSART) {
        this.aNTRIEBSART = aNTRIEBSART;
    }

    public TurboliftSchacht getTurboliftschacht() {
        return turboliftschacht;
    }

    public void setTurboliftschacht(TurboliftSchacht turboliftschacht) {
        this.turboliftschacht = turboliftschacht;
    }

}