





import java.util.List;
import java.util.ArrayList;

public class shr5_PersonaZauber extends Erlernbar {

    private int stufe;





    private shr5_Zauber shr5_zauber;




    private shr5_Zauberer shr5_zauberer;


    public shr5_PersonaZauber(
        int stufe    ) {
        super(
        );
        this.stufe = stufe;
    }


    public int getStufe() {
        return stufe;
    }

    public void setStufe(int stufe) {
        this.stufe = stufe;
    }

    public shr5_Zauber getShr5_zauber() {
        return shr5_zauber;
    }

    public void setShr5_zauber(shr5_Zauber shr5_zauber) {
        this.shr5_zauber = shr5_zauber;
    }
    public shr5_Zauberer getShr5_zauberer() {
        return shr5_zauberer;
    }

    public void setShr5_zauberer(shr5_Zauberer shr5_zauberer) {
        this.shr5_zauberer = shr5_zauberer;
    }

}