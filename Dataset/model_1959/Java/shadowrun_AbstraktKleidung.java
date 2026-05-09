





import java.util.List;
import java.util.ArrayList;

public class shadowrun_AbstraktKleidung extends AbstaktGegenstand {

    private String koeperTeil;





    private shadowrun_AbstaktPersona shadowrun_abstaktpersona;


    public shadowrun_AbstraktKleidung(
        String koeperTeil    ) {
        super(
        );
        this.koeperTeil = koeperTeil;
    }


    public String getKoeperteil() {
        return koeperTeil;
    }

    public void setKoeperteil(String koeperTeil) {
        this.koeperTeil = koeperTeil;
    }

    public shadowrun_AbstaktPersona getShadowrun_abstaktpersona() {
        return shadowrun_abstaktpersona;
    }

    public void setShadowrun_abstaktpersona(shadowrun_AbstaktPersona shadowrun_abstaktpersona) {
        this.shadowrun_abstaktpersona = shadowrun_abstaktpersona;
    }

}