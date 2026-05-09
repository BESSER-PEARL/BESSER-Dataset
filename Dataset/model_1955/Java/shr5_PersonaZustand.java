





import java.util.List;
import java.util.ArrayList;

public class shr5_PersonaZustand  {

    private int zustandKoerperlichMax;
    private int zustandGeistigMax;
    private int zustandGrenze;



    public shr5_PersonaZustand(
        int zustandKoerperlichMax,        int zustandGeistigMax,        int zustandGrenze    ) {
        this.zustandKoerperlichMax = zustandKoerperlichMax;
        this.zustandGeistigMax = zustandGeistigMax;
        this.zustandGrenze = zustandGrenze;
    }


    public int getZustandkoerperlichmax() {
        return zustandKoerperlichMax;
    }

    public void setZustandkoerperlichmax(int zustandKoerperlichMax) {
        this.zustandKoerperlichMax = zustandKoerperlichMax;
    }
    public int getZustandgeistigmax() {
        return zustandGeistigMax;
    }

    public void setZustandgeistigmax(int zustandGeistigMax) {
        this.zustandGeistigMax = zustandGeistigMax;
    }
    public int getZustandgrenze() {
        return zustandGrenze;
    }

    public void setZustandgrenze(int zustandGrenze) {
        this.zustandGrenze = zustandGrenze;
    }


}