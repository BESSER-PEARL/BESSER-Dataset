





import java.util.List;
import java.util.ArrayList;

public class shr5_Geist extends AstraleProjektion, StufenPersona {

    private int staerkeBasis;
    private int logikBasis;
    private int charismaBasis;
    private int intuitionBasis;
    private int konstitutionBasis;
    private int geschicklichkeitBasis;
    private int willenskraftBasis;
    private int reaktionBasis;



    public shr5_Geist(
        int staerkeBasis,        int logikBasis,        int charismaBasis,        int intuitionBasis,        int konstitutionBasis,        int geschicklichkeitBasis,        int willenskraftBasis,        int reaktionBasis    ) {
        super(
        );
        this.staerkeBasis = staerkeBasis;
        this.logikBasis = logikBasis;
        this.charismaBasis = charismaBasis;
        this.intuitionBasis = intuitionBasis;
        this.konstitutionBasis = konstitutionBasis;
        this.geschicklichkeitBasis = geschicklichkeitBasis;
        this.willenskraftBasis = willenskraftBasis;
        this.reaktionBasis = reaktionBasis;
    }


    public int getStaerkebasis() {
        return staerkeBasis;
    }

    public void setStaerkebasis(int staerkeBasis) {
        this.staerkeBasis = staerkeBasis;
    }
    public int getLogikbasis() {
        return logikBasis;
    }

    public void setLogikbasis(int logikBasis) {
        this.logikBasis = logikBasis;
    }
    public int getCharismabasis() {
        return charismaBasis;
    }

    public void setCharismabasis(int charismaBasis) {
        this.charismaBasis = charismaBasis;
    }
    public int getIntuitionbasis() {
        return intuitionBasis;
    }

    public void setIntuitionbasis(int intuitionBasis) {
        this.intuitionBasis = intuitionBasis;
    }
    public int getKonstitutionbasis() {
        return konstitutionBasis;
    }

    public void setKonstitutionbasis(int konstitutionBasis) {
        this.konstitutionBasis = konstitutionBasis;
    }
    public int getGeschicklichkeitbasis() {
        return geschicklichkeitBasis;
    }

    public void setGeschicklichkeitbasis(int geschicklichkeitBasis) {
        this.geschicklichkeitBasis = geschicklichkeitBasis;
    }
    public int getWillenskraftbasis() {
        return willenskraftBasis;
    }

    public void setWillenskraftbasis(int willenskraftBasis) {
        this.willenskraftBasis = willenskraftBasis;
    }
    public int getReaktionbasis() {
        return reaktionBasis;
    }

    public void setReaktionbasis(int reaktionBasis) {
        this.reaktionBasis = reaktionBasis;
    }


}