





import java.util.List;
import java.util.ArrayList;

public class shr5_Schutzgeist extends MagischeMods {

    private String nachteile;
    private String vorteile;





    private shr5_MagischePersona shr5_magischepersona;


    public shr5_Schutzgeist(
        String nachteile,        String vorteile    ) {
        super(
        );
        this.nachteile = nachteile;
        this.vorteile = vorteile;
    }


    public String getNachteile() {
        return nachteile;
    }

    public void setNachteile(String nachteile) {
        this.nachteile = nachteile;
    }
    public String getVorteile() {
        return vorteile;
    }

    public void setVorteile(String vorteile) {
        this.vorteile = vorteile;
    }

    public shr5_MagischePersona getShr5_magischepersona() {
        return shr5_magischepersona;
    }

    public void setShr5_magischepersona(shr5_MagischePersona shr5_magischepersona) {
        this.shr5_magischepersona = shr5_magischepersona;
    }

}