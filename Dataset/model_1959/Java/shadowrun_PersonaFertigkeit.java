





import java.util.List;
import java.util.ArrayList;

public class shadowrun_PersonaFertigkeit  {

    private int stufe;





    private shadowrun_AbstaktPersona shadowrun_abstaktpersona;




    private shadowrun_AbstraktFertigkeit shadowrun_abstraktfertigkeit;


    public shadowrun_PersonaFertigkeit(
        int stufe    ) {
        this.stufe = stufe;
    }


    public int getStufe() {
        return stufe;
    }

    public void setStufe(int stufe) {
        this.stufe = stufe;
    }

    public shadowrun_AbstaktPersona getShadowrun_abstaktpersona() {
        return shadowrun_abstaktpersona;
    }

    public void setShadowrun_abstaktpersona(shadowrun_AbstaktPersona shadowrun_abstaktpersona) {
        this.shadowrun_abstaktpersona = shadowrun_abstaktpersona;
    }
    public shadowrun_AbstraktFertigkeit getShadowrun_abstraktfertigkeit() {
        return shadowrun_abstraktfertigkeit;
    }

    public void setShadowrun_abstraktfertigkeit(shadowrun_AbstraktFertigkeit shadowrun_abstraktfertigkeit) {
        this.shadowrun_abstraktfertigkeit = shadowrun_abstraktfertigkeit;
    }

}