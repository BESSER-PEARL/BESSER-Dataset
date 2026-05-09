





import java.util.List;
import java.util.ArrayList;

public class shadowrun_AbstaktPersona extends Beschreibbar, KoerperlicheAtribute, GeistigeAttribute, BodyIndex, BerechneteAttribute, Essenz {

    private int WillenskraftBase;
    private int ReaktionWBase;
    private int ReaktionBase;
    private int SchnelligkeitBase;
    private int eigenGewicht;
    private int CharismaBase;
    private int KonsitutionBase;
    private int KampfpoolBase;
    private int EssenzBase;
    private int StaerkeBase;
    private String modsetter;
    private int InteligenzBase;



    public shadowrun_AbstaktPersona(
        int WillenskraftBase,        int ReaktionWBase,        int ReaktionBase,        int SchnelligkeitBase,        int eigenGewicht,        int CharismaBase,        int KonsitutionBase,        int KampfpoolBase,        int EssenzBase,        int StaerkeBase,        String modsetter,        int InteligenzBase    ) {
        super(
        );
        this.WillenskraftBase = WillenskraftBase;
        this.ReaktionWBase = ReaktionWBase;
        this.ReaktionBase = ReaktionBase;
        this.SchnelligkeitBase = SchnelligkeitBase;
        this.eigenGewicht = eigenGewicht;
        this.CharismaBase = CharismaBase;
        this.KonsitutionBase = KonsitutionBase;
        this.KampfpoolBase = KampfpoolBase;
        this.EssenzBase = EssenzBase;
        this.StaerkeBase = StaerkeBase;
        this.modsetter = modsetter;
        this.InteligenzBase = InteligenzBase;
    }


    public int getWillenskraftbase() {
        return WillenskraftBase;
    }

    public void setWillenskraftbase(int WillenskraftBase) {
        this.WillenskraftBase = WillenskraftBase;
    }
    public int getReaktionwbase() {
        return ReaktionWBase;
    }

    public void setReaktionwbase(int ReaktionWBase) {
        this.ReaktionWBase = ReaktionWBase;
    }
    public int getReaktionbase() {
        return ReaktionBase;
    }

    public void setReaktionbase(int ReaktionBase) {
        this.ReaktionBase = ReaktionBase;
    }
    public int getSchnelligkeitbase() {
        return SchnelligkeitBase;
    }

    public void setSchnelligkeitbase(int SchnelligkeitBase) {
        this.SchnelligkeitBase = SchnelligkeitBase;
    }
    public int getEigengewicht() {
        return eigenGewicht;
    }

    public void setEigengewicht(int eigenGewicht) {
        this.eigenGewicht = eigenGewicht;
    }
    public int getCharismabase() {
        return CharismaBase;
    }

    public void setCharismabase(int CharismaBase) {
        this.CharismaBase = CharismaBase;
    }
    public int getKonsitutionbase() {
        return KonsitutionBase;
    }

    public void setKonsitutionbase(int KonsitutionBase) {
        this.KonsitutionBase = KonsitutionBase;
    }
    public int getKampfpoolbase() {
        return KampfpoolBase;
    }

    public void setKampfpoolbase(int KampfpoolBase) {
        this.KampfpoolBase = KampfpoolBase;
    }
    public int getEssenzbase() {
        return EssenzBase;
    }

    public void setEssenzbase(int EssenzBase) {
        this.EssenzBase = EssenzBase;
    }
    public int getStaerkebase() {
        return StaerkeBase;
    }

    public void setStaerkebase(int StaerkeBase) {
        this.StaerkeBase = StaerkeBase;
    }
    public String getModsetter() {
        return modsetter;
    }

    public void setModsetter(String modsetter) {
        this.modsetter = modsetter;
    }
    public int getInteligenzbase() {
        return InteligenzBase;
    }

    public void setInteligenzbase(int InteligenzBase) {
        this.InteligenzBase = InteligenzBase;
    }


}