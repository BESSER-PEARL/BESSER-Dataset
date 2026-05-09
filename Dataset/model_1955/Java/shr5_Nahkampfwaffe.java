





import java.util.List;
import java.util.ArrayList;

public class shr5_Nahkampfwaffe extends AbstaktWaffe {

    private int reichweite;





    private shr5_Spezies shr5_spezies;


    public shr5_Nahkampfwaffe(
        int reichweite    ) {
        super(
        );
        this.reichweite = reichweite;
    }


    public int getReichweite() {
        return reichweite;
    }

    public void setReichweite(int reichweite) {
        this.reichweite = reichweite;
    }

    public shr5_Spezies getShr5_spezies() {
        return shr5_spezies;
    }

    public void setShr5_spezies(shr5_Spezies shr5_spezies) {
        this.shr5_spezies = shr5_spezies;
    }

}