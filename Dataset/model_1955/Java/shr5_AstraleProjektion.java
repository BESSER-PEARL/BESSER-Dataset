





import java.util.List;
import java.util.ArrayList;

public class shr5_AstraleProjektion  {

    private int astralesLimit;
    private int astraleInitative;
    private int astraleInitativWuerfel;
    private int astraleKonstitution;
    private int astraleGeschicklichkeit;
    private int astraleStaerke;
    private int astralePanzerung;
    private int astraleReaktion;



    public shr5_AstraleProjektion(
        int astralesLimit,        int astraleInitative,        int astraleInitativWuerfel,        int astraleKonstitution,        int astraleGeschicklichkeit,        int astraleStaerke,        int astralePanzerung,        int astraleReaktion    ) {
        this.astralesLimit = astralesLimit;
        this.astraleInitative = astraleInitative;
        this.astraleInitativWuerfel = astraleInitativWuerfel;
        this.astraleKonstitution = astraleKonstitution;
        this.astraleGeschicklichkeit = astraleGeschicklichkeit;
        this.astraleStaerke = astraleStaerke;
        this.astralePanzerung = astralePanzerung;
        this.astraleReaktion = astraleReaktion;
    }


    public int getAstraleslimit() {
        return astralesLimit;
    }

    public void setAstraleslimit(int astralesLimit) {
        this.astralesLimit = astralesLimit;
    }
    public int getAstraleinitative() {
        return astraleInitative;
    }

    public void setAstraleinitative(int astraleInitative) {
        this.astraleInitative = astraleInitative;
    }
    public int getAstraleinitativwuerfel() {
        return astraleInitativWuerfel;
    }

    public void setAstraleinitativwuerfel(int astraleInitativWuerfel) {
        this.astraleInitativWuerfel = astraleInitativWuerfel;
    }
    public int getAstralekonstitution() {
        return astraleKonstitution;
    }

    public void setAstralekonstitution(int astraleKonstitution) {
        this.astraleKonstitution = astraleKonstitution;
    }
    public int getAstralegeschicklichkeit() {
        return astraleGeschicklichkeit;
    }

    public void setAstralegeschicklichkeit(int astraleGeschicklichkeit) {
        this.astraleGeschicklichkeit = astraleGeschicklichkeit;
    }
    public int getAstralestaerke() {
        return astraleStaerke;
    }

    public void setAstralestaerke(int astraleStaerke) {
        this.astraleStaerke = astraleStaerke;
    }
    public int getAstralepanzerung() {
        return astralePanzerung;
    }

    public void setAstralepanzerung(int astralePanzerung) {
        this.astralePanzerung = astralePanzerung;
    }
    public int getAstralereaktion() {
        return astraleReaktion;
    }

    public void setAstralereaktion(int astraleReaktion) {
        this.astraleReaktion = astraleReaktion;
    }


}