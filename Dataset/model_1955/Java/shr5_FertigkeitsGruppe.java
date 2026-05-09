





import java.util.List;
import java.util.ArrayList;

public class shr5_FertigkeitsGruppe extends Quelle, Beschreibbar, Modifyable {






    private shr5_StufenPersona shr5_stufenpersona;




    private shr5_AspektMagier shr5_aspektmagier;


    public shr5_FertigkeitsGruppe(
    ) {
        super(
        );
    }



    public shr5_StufenPersona getShr5_stufenpersona() {
        return shr5_stufenpersona;
    }

    public void setShr5_stufenpersona(shr5_StufenPersona shr5_stufenpersona) {
        this.shr5_stufenpersona = shr5_stufenpersona;
    }
    public shr5_AspektMagier getShr5_aspektmagier() {
        return shr5_aspektmagier;
    }

    public void setShr5_aspektmagier(shr5_AspektMagier shr5_aspektmagier) {
        this.shr5_aspektmagier = shr5_aspektmagier;
    }

}