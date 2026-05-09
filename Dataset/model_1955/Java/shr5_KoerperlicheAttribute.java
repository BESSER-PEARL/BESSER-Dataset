





import java.util.List;
import java.util.ArrayList;

public class shr5_KoerperlicheAttribute extends ModifikatorAttribute {

    private int reaktion;
    private int staerke;
    private int konstitution;
    private int geschicklichkeit;



    public shr5_KoerperlicheAttribute(
        int reaktion,        int staerke,        int konstitution,        int geschicklichkeit    ) {
        super(
        );
        this.reaktion = reaktion;
        this.staerke = staerke;
        this.konstitution = konstitution;
        this.geschicklichkeit = geschicklichkeit;
    }


    public int getReaktion() {
        return reaktion;
    }

    public void setReaktion(int reaktion) {
        this.reaktion = reaktion;
    }
    public int getStaerke() {
        return staerke;
    }

    public void setStaerke(int staerke) {
        this.staerke = staerke;
    }
    public int getKonstitution() {
        return konstitution;
    }

    public void setKonstitution(int konstitution) {
        this.konstitution = konstitution;
    }
    public int getGeschicklichkeit() {
        return geschicklichkeit;
    }

    public void setGeschicklichkeit(int geschicklichkeit) {
        this.geschicklichkeit = geschicklichkeit;
    }


}