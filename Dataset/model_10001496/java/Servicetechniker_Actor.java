





import java.util.List;
import java.util.ArrayList;

public class Servicetechniker_Actor  {






    private Hilfe_rufen_external hilfe_rufen_external;




    private Auswahl_der_Fahrkartenkategorie_external auswahl_der_fahrkartenkategorie_external;




    private Kunde_Actor kunde_actor;




    private Wartung_external wartung_external;


    public Servicetechniker_Actor(
    ) {
    }



    public Hilfe_rufen_external getHilfe_rufen_external() {
        return hilfe_rufen_external;
    }

    public void setHilfe_rufen_external(Hilfe_rufen_external hilfe_rufen_external) {
        this.hilfe_rufen_external = hilfe_rufen_external;
    }
    public Auswahl_der_Fahrkartenkategorie_external getAuswahl_der_fahrkartenkategorie_external() {
        return auswahl_der_fahrkartenkategorie_external;
    }

    public void setAuswahl_der_fahrkartenkategorie_external(Auswahl_der_Fahrkartenkategorie_external auswahl_der_fahrkartenkategorie_external) {
        this.auswahl_der_fahrkartenkategorie_external = auswahl_der_fahrkartenkategorie_external;
    }
    public Kunde_Actor getKunde_actor() {
        return kunde_actor;
    }

    public void setKunde_actor(Kunde_Actor kunde_actor) {
        this.kunde_actor = kunde_actor;
    }
    public Wartung_external getWartung_external() {
        return wartung_external;
    }

    public void setWartung_external(Wartung_external wartung_external) {
        this.wartung_external = wartung_external;
    }

}