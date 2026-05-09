





import java.util.List;
import java.util.ArrayList;

public class shadowrun_Zauber extends Beschreibbar {

    private String Enzug;
    private String Mindestwurf;
    private String Dauer;
    private String Schaden;
    private String art;
    private String reichweite;



    public shadowrun_Zauber(
        String Enzug,        String Mindestwurf,        String Dauer,        String Schaden,        String art,        String reichweite    ) {
        super(
        );
        this.Enzug = Enzug;
        this.Mindestwurf = Mindestwurf;
        this.Dauer = Dauer;
        this.Schaden = Schaden;
        this.art = art;
        this.reichweite = reichweite;
    }


    public String getEnzug() {
        return Enzug;
    }

    public void setEnzug(String Enzug) {
        this.Enzug = Enzug;
    }
    public String getMindestwurf() {
        return Mindestwurf;
    }

    public void setMindestwurf(String Mindestwurf) {
        this.Mindestwurf = Mindestwurf;
    }
    public String getDauer() {
        return Dauer;
    }

    public void setDauer(String Dauer) {
        this.Dauer = Dauer;
    }
    public String getSchaden() {
        return Schaden;
    }

    public void setSchaden(String Schaden) {
        this.Schaden = Schaden;
    }
    public String getArt() {
        return art;
    }

    public void setArt(String art) {
        this.art = art;
    }
    public String getReichweite() {
        return reichweite;
    }

    public void setReichweite(String reichweite) {
        this.reichweite = reichweite;
    }


}