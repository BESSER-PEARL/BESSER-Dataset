





import java.util.List;
import java.util.ArrayList;

public class shadowrun_Spezies extends Modifizierbar, Beschreibbar {

    private int CharismaMax;
    private int WillenskraftMax;
    private int KonsitutionMax;
    private int SchnelligkeitMax;
    private int InteligenzMax;
    private int StaerkeMax;





    private shadowrun_AbstaktPersona shadowrun_abstaktpersona;


    public shadowrun_Spezies(
        int CharismaMax,        int WillenskraftMax,        int KonsitutionMax,        int SchnelligkeitMax,        int InteligenzMax,        int StaerkeMax    ) {
        super(
        );
        this.CharismaMax = CharismaMax;
        this.WillenskraftMax = WillenskraftMax;
        this.KonsitutionMax = KonsitutionMax;
        this.SchnelligkeitMax = SchnelligkeitMax;
        this.InteligenzMax = InteligenzMax;
        this.StaerkeMax = StaerkeMax;
    }


    public int getCharismamax() {
        return CharismaMax;
    }

    public void setCharismamax(int CharismaMax) {
        this.CharismaMax = CharismaMax;
    }
    public int getWillenskraftmax() {
        return WillenskraftMax;
    }

    public void setWillenskraftmax(int WillenskraftMax) {
        this.WillenskraftMax = WillenskraftMax;
    }
    public int getKonsitutionmax() {
        return KonsitutionMax;
    }

    public void setKonsitutionmax(int KonsitutionMax) {
        this.KonsitutionMax = KonsitutionMax;
    }
    public int getSchnelligkeitmax() {
        return SchnelligkeitMax;
    }

    public void setSchnelligkeitmax(int SchnelligkeitMax) {
        this.SchnelligkeitMax = SchnelligkeitMax;
    }
    public int getInteligenzmax() {
        return InteligenzMax;
    }

    public void setInteligenzmax(int InteligenzMax) {
        this.InteligenzMax = InteligenzMax;
    }
    public int getStaerkemax() {
        return StaerkeMax;
    }

    public void setStaerkemax(int StaerkeMax) {
        this.StaerkeMax = StaerkeMax;
    }

    public shadowrun_AbstaktPersona getShadowrun_abstaktpersona() {
        return shadowrun_abstaktpersona;
    }

    public void setShadowrun_abstaktpersona(shadowrun_AbstaktPersona shadowrun_abstaktpersona) {
        this.shadowrun_abstaktpersona = shadowrun_abstaktpersona;
    }

}