





import java.util.List;
import java.util.ArrayList;

public class shadowrun_KoerperlicheAtribute extends Schadenswiederstand {

    private int Schnelligkeit;
    private int Staerke;
    private int Konsitution;



    public shadowrun_KoerperlicheAtribute(
        int Schnelligkeit,        int Staerke,        int Konsitution    ) {
        super(
        );
        this.Schnelligkeit = Schnelligkeit;
        this.Staerke = Staerke;
        this.Konsitution = Konsitution;
    }


    public int getSchnelligkeit() {
        return Schnelligkeit;
    }

    public void setSchnelligkeit(int Schnelligkeit) {
        this.Schnelligkeit = Schnelligkeit;
    }
    public int getStaerke() {
        return Staerke;
    }

    public void setStaerke(int Staerke) {
        this.Staerke = Staerke;
    }
    public int getKonsitution() {
        return Konsitution;
    }

    public void setKonsitution(int Konsitution) {
        this.Konsitution = Konsitution;
    }


}