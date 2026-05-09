





import java.util.List;
import java.util.ArrayList;

public class shr5_PersonaFertigkeit extends Steigerbar {






    private shr5_Fertigkeit shr5_fertigkeit;




    private List<shr5_Spezialisierung> shr5_spezialisierungs;




    private shr5_AbstraktPersona shr5_abstraktpersona;


    public shr5_PersonaFertigkeit(
    ) {
        super(
        );
        this.shr5_spezialisierungs = new ArrayList<>();
    }

    public shr5_PersonaFertigkeit(
        ArrayList<shr5_Spezialisierung> shr5_spezialisierungs    ) {
        this.shr5_spezialisierungs = shr5_spezialisierungs;
    }


    public shr5_Fertigkeit getShr5_fertigkeit() {
        return shr5_fertigkeit;
    }

    public void setShr5_fertigkeit(shr5_Fertigkeit shr5_fertigkeit) {
        this.shr5_fertigkeit = shr5_fertigkeit;
    }
    public List<shr5_Spezialisierung> getShr5_spezialisierungs() {
        return shr5_spezialisierungs;
    }

    public void addShr5_spezialisierung(Shr5_spezialisierung shr5_spezialisierung) {
        this.shr5_spezialisierungs.add(shr5_spezialisierung);
    }
    public shr5_AbstraktPersona getShr5_abstraktpersona() {
        return shr5_abstraktpersona;
    }

    public void setShr5_abstraktpersona(shr5_AbstraktPersona shr5_abstraktpersona) {
        this.shr5_abstraktpersona = shr5_abstraktpersona;
    }

}