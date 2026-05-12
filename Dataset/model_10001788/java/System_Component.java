





import java.util.List;
import java.util.ArrayList;

public class System_Component  {






    private Comptable_Actor comptable_actor;




    private __Syst_me___Banques_Actor __syst_me___banques_actor;




    private G_rant_Actor g_rant_actor;




    private Logistique_Actor logistique_actor;




    private Livreur_Actor livreur_actor;




    private __Syst_me___GPS_Actor __syst_me___gps_actor;


    public System_Component(
    ) {
    }



    public Comptable_Actor getComptable_actor() {
        return comptable_actor;
    }

    public void setComptable_actor(Comptable_Actor comptable_actor) {
        this.comptable_actor = comptable_actor;
    }
    public __Syst_me___Banques_Actor get__syst_me___banques_actor() {
        return __syst_me___banques_actor;
    }

    public void set__syst_me___banques_actor(__Syst_me___Banques_Actor __syst_me___banques_actor) {
        this.__syst_me___banques_actor = __syst_me___banques_actor;
    }
    public G_rant_Actor getG_rant_actor() {
        return g_rant_actor;
    }

    public void setG_rant_actor(G_rant_Actor g_rant_actor) {
        this.g_rant_actor = g_rant_actor;
    }
    public Logistique_Actor getLogistique_actor() {
        return logistique_actor;
    }

    public void setLogistique_actor(Logistique_Actor logistique_actor) {
        this.logistique_actor = logistique_actor;
    }
    public Livreur_Actor getLivreur_actor() {
        return livreur_actor;
    }

    public void setLivreur_actor(Livreur_Actor livreur_actor) {
        this.livreur_actor = livreur_actor;
    }
    public __Syst_me___GPS_Actor get__syst_me___gps_actor() {
        return __syst_me___gps_actor;
    }

    public void set__syst_me___gps_actor(__Syst_me___GPS_Actor __syst_me___gps_actor) {
        this.__syst_me___gps_actor = __syst_me___gps_actor;
    }

}