





import java.util.List;
import java.util.ArrayList;

public class shr5_KoerperPersona extends Panzerung, PersonaZustand, AbstraktPersona, BerechneteAttribute {

    private int zustandGeistig;
    private int zustandKoerperlich;





    private List<shr5_PersonaEigenschaft> shr5_personaeigenschafts;




    private List<shr5_Koerpermods> shr5_koerpermodss;


    public shr5_KoerperPersona(
        int zustandGeistig,        int zustandKoerperlich    ) {
        super(
        );
        this.zustandGeistig = zustandGeistig;
        this.zustandKoerperlich = zustandKoerperlich;
        this.shr5_personaeigenschafts = new ArrayList<>();
        this.shr5_koerpermodss = new ArrayList<>();
    }

    public shr5_KoerperPersona(
        int zustandGeistig,        int zustandKoerperlich        ArrayList<shr5_PersonaEigenschaft> shr5_personaeigenschafts,        ArrayList<shr5_Koerpermods> shr5_koerpermodss    ) {
        this.zustandGeistig = zustandGeistig;
        this.zustandKoerperlich = zustandKoerperlich;
        this.shr5_personaeigenschafts = shr5_personaeigenschafts;
        this.shr5_koerpermodss = shr5_koerpermodss;
    }

    public int getZustandgeistig() {
        return zustandGeistig;
    }

    public void setZustandgeistig(int zustandGeistig) {
        this.zustandGeistig = zustandGeistig;
    }
    public int getZustandkoerperlich() {
        return zustandKoerperlich;
    }

    public void setZustandkoerperlich(int zustandKoerperlich) {
        this.zustandKoerperlich = zustandKoerperlich;
    }

    public List<shr5_PersonaEigenschaft> getShr5_personaeigenschafts() {
        return shr5_personaeigenschafts;
    }

    public void addShr5_personaeigenschaft(Shr5_personaeigenschaft shr5_personaeigenschaft) {
        this.shr5_personaeigenschafts.add(shr5_personaeigenschaft);
    }
    public List<shr5_Koerpermods> getShr5_koerpermodss() {
        return shr5_koerpermodss;
    }

    public void addShr5_koerpermods(Shr5_koerpermods shr5_koerpermods) {
        this.shr5_koerpermodss.add(shr5_koerpermods);
    }

}