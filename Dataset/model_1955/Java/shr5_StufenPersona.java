





import java.util.List;
import java.util.ArrayList;

public class shr5_StufenPersona extends Panzerung, Quelle, SpezielleAttribute, ChrakterLimits, Beschreibbar, KoerperlicheAttribute, GeistigeAttribute {

    private int stufe;



    public shr5_StufenPersona(
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


}