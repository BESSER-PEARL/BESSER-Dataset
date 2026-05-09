





import java.util.List;
import java.util.ArrayList;

public class shr5_ChrakterLimits  {

    private int geistig;
    private int sozial;
    private int koerperlich;



    public shr5_ChrakterLimits(
        int geistig,        int sozial,        int koerperlich    ) {
        this.geistig = geistig;
        this.sozial = sozial;
        this.koerperlich = koerperlich;
    }


    public int getGeistig() {
        return geistig;
    }

    public void setGeistig(int geistig) {
        this.geistig = geistig;
    }
    public int getSozial() {
        return sozial;
    }

    public void setSozial(int sozial) {
        this.sozial = sozial;
    }
    public int getKoerperlich() {
        return koerperlich;
    }

    public void setKoerperlich(int koerperlich) {
        this.koerperlich = koerperlich;
    }


}