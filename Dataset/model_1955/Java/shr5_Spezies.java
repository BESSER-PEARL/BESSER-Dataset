





import java.util.List;
import java.util.ArrayList;

public class shr5_Spezies extends Quelle, Beschreibbar, Modifizierbar {

    private int magieMax;
    private int logikMin;
    private int geschicklichkeitMin;
    private int intuitionMin;
    private int staerkeMax;
    private int laufen;
    private int resonanzMin;
    private int willenskraftMax;
    private int intuitionMax;
    private int resonanzMax;
    private int konstitutionMin;
    private int rennen;
    private int sprinten;
    private int reaktionMin;
    private int staerkeMin;
    private int essenzMax;
    private int charismaMax;
    private int essenzMin;
    private int charismaMin;
    private int konstitutionMax;
    private int edgeMax;
    private int willenskraftMin;
    private int reaktionMax;
    private int logikMax;
    private int edgeMin;
    private int geschicklichkeitMax;
    private int magieMin;



    public shr5_Spezies(
        int magieMax,        int logikMin,        int geschicklichkeitMin,        int intuitionMin,        int staerkeMax,        int laufen,        int resonanzMin,        int willenskraftMax,        int intuitionMax,        int resonanzMax,        int konstitutionMin,        int rennen,        int sprinten,        int reaktionMin,        int staerkeMin,        int essenzMax,        int charismaMax,        int essenzMin,        int charismaMin,        int konstitutionMax,        int edgeMax,        int willenskraftMin,        int reaktionMax,        int logikMax,        int edgeMin,        int geschicklichkeitMax,        int magieMin    ) {
        super(
        );
        this.magieMax = magieMax;
        this.logikMin = logikMin;
        this.geschicklichkeitMin = geschicklichkeitMin;
        this.intuitionMin = intuitionMin;
        this.staerkeMax = staerkeMax;
        this.laufen = laufen;
        this.resonanzMin = resonanzMin;
        this.willenskraftMax = willenskraftMax;
        this.intuitionMax = intuitionMax;
        this.resonanzMax = resonanzMax;
        this.konstitutionMin = konstitutionMin;
        this.rennen = rennen;
        this.sprinten = sprinten;
        this.reaktionMin = reaktionMin;
        this.staerkeMin = staerkeMin;
        this.essenzMax = essenzMax;
        this.charismaMax = charismaMax;
        this.essenzMin = essenzMin;
        this.charismaMin = charismaMin;
        this.konstitutionMax = konstitutionMax;
        this.edgeMax = edgeMax;
        this.willenskraftMin = willenskraftMin;
        this.reaktionMax = reaktionMax;
        this.logikMax = logikMax;
        this.edgeMin = edgeMin;
        this.geschicklichkeitMax = geschicklichkeitMax;
        this.magieMin = magieMin;
    }


    public int getMagiemax() {
        return magieMax;
    }

    public void setMagiemax(int magieMax) {
        this.magieMax = magieMax;
    }
    public int getLogikmin() {
        return logikMin;
    }

    public void setLogikmin(int logikMin) {
        this.logikMin = logikMin;
    }
    public int getGeschicklichkeitmin() {
        return geschicklichkeitMin;
    }

    public void setGeschicklichkeitmin(int geschicklichkeitMin) {
        this.geschicklichkeitMin = geschicklichkeitMin;
    }
    public int getIntuitionmin() {
        return intuitionMin;
    }

    public void setIntuitionmin(int intuitionMin) {
        this.intuitionMin = intuitionMin;
    }
    public int getStaerkemax() {
        return staerkeMax;
    }

    public void setStaerkemax(int staerkeMax) {
        this.staerkeMax = staerkeMax;
    }
    public int getLaufen() {
        return laufen;
    }

    public void setLaufen(int laufen) {
        this.laufen = laufen;
    }
    public int getResonanzmin() {
        return resonanzMin;
    }

    public void setResonanzmin(int resonanzMin) {
        this.resonanzMin = resonanzMin;
    }
    public int getWillenskraftmax() {
        return willenskraftMax;
    }

    public void setWillenskraftmax(int willenskraftMax) {
        this.willenskraftMax = willenskraftMax;
    }
    public int getIntuitionmax() {
        return intuitionMax;
    }

    public void setIntuitionmax(int intuitionMax) {
        this.intuitionMax = intuitionMax;
    }
    public int getResonanzmax() {
        return resonanzMax;
    }

    public void setResonanzmax(int resonanzMax) {
        this.resonanzMax = resonanzMax;
    }
    public int getKonstitutionmin() {
        return konstitutionMin;
    }

    public void setKonstitutionmin(int konstitutionMin) {
        this.konstitutionMin = konstitutionMin;
    }
    public int getRennen() {
        return rennen;
    }

    public void setRennen(int rennen) {
        this.rennen = rennen;
    }
    public int getSprinten() {
        return sprinten;
    }

    public void setSprinten(int sprinten) {
        this.sprinten = sprinten;
    }
    public int getReaktionmin() {
        return reaktionMin;
    }

    public void setReaktionmin(int reaktionMin) {
        this.reaktionMin = reaktionMin;
    }
    public int getStaerkemin() {
        return staerkeMin;
    }

    public void setStaerkemin(int staerkeMin) {
        this.staerkeMin = staerkeMin;
    }
    public int getEssenzmax() {
        return essenzMax;
    }

    public void setEssenzmax(int essenzMax) {
        this.essenzMax = essenzMax;
    }
    public int getCharismamax() {
        return charismaMax;
    }

    public void setCharismamax(int charismaMax) {
        this.charismaMax = charismaMax;
    }
    public int getEssenzmin() {
        return essenzMin;
    }

    public void setEssenzmin(int essenzMin) {
        this.essenzMin = essenzMin;
    }
    public int getCharismamin() {
        return charismaMin;
    }

    public void setCharismamin(int charismaMin) {
        this.charismaMin = charismaMin;
    }
    public int getKonstitutionmax() {
        return konstitutionMax;
    }

    public void setKonstitutionmax(int konstitutionMax) {
        this.konstitutionMax = konstitutionMax;
    }
    public int getEdgemax() {
        return edgeMax;
    }

    public void setEdgemax(int edgeMax) {
        this.edgeMax = edgeMax;
    }
    public int getWillenskraftmin() {
        return willenskraftMin;
    }

    public void setWillenskraftmin(int willenskraftMin) {
        this.willenskraftMin = willenskraftMin;
    }
    public int getReaktionmax() {
        return reaktionMax;
    }

    public void setReaktionmax(int reaktionMax) {
        this.reaktionMax = reaktionMax;
    }
    public int getLogikmax() {
        return logikMax;
    }

    public void setLogikmax(int logikMax) {
        this.logikMax = logikMax;
    }
    public int getEdgemin() {
        return edgeMin;
    }

    public void setEdgemin(int edgeMin) {
        this.edgeMin = edgeMin;
    }
    public int getGeschicklichkeitmax() {
        return geschicklichkeitMax;
    }

    public void setGeschicklichkeitmax(int geschicklichkeitMax) {
        this.geschicklichkeitMax = geschicklichkeitMax;
    }
    public int getMagiemin() {
        return magieMin;
    }

    public void setMagiemin(int magieMin) {
        this.magieMin = magieMin;
    }


}