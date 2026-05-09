





import java.util.List;
import java.util.ArrayList;

public class shr5_AbstraktPersona extends SpezielleAttribute, ChrakterLimits, Beschreibbar, KoerperlicheAttribute, GeistigeAttribute {

    private String modManager;
    private int logikBasis;
    private int willenskraftBasis;
    private int staerkeBasis;
    private int charismaBasis;
    private int reaktionBasis;
    private int intuitionBasis;
    private int konstitutionBasis;
    private int geschicklichkeitBasis;





    private shr5_Spezies shr5_spezies;




    private List<shr5_PersonaMartialartStyle> shr5_personamartialartstyles;


    public shr5_AbstraktPersona(
        String modManager,        int logikBasis,        int willenskraftBasis,        int staerkeBasis,        int charismaBasis,        int reaktionBasis,        int intuitionBasis,        int konstitutionBasis,        int geschicklichkeitBasis    ) {
        super(
        );
        this.modManager = modManager;
        this.logikBasis = logikBasis;
        this.willenskraftBasis = willenskraftBasis;
        this.staerkeBasis = staerkeBasis;
        this.charismaBasis = charismaBasis;
        this.reaktionBasis = reaktionBasis;
        this.intuitionBasis = intuitionBasis;
        this.konstitutionBasis = konstitutionBasis;
        this.geschicklichkeitBasis = geschicklichkeitBasis;
        this.shr5_personamartialartstyles = new ArrayList<>();
    }

    public shr5_AbstraktPersona(
        String modManager,        int logikBasis,        int willenskraftBasis,        int staerkeBasis,        int charismaBasis,        int reaktionBasis,        int intuitionBasis,        int konstitutionBasis,        int geschicklichkeitBasis        ArrayList<shr5_PersonaMartialartStyle> shr5_personamartialartstyles    ) {
        this.modManager = modManager;
        this.logikBasis = logikBasis;
        this.willenskraftBasis = willenskraftBasis;
        this.staerkeBasis = staerkeBasis;
        this.charismaBasis = charismaBasis;
        this.reaktionBasis = reaktionBasis;
        this.intuitionBasis = intuitionBasis;
        this.konstitutionBasis = konstitutionBasis;
        this.geschicklichkeitBasis = geschicklichkeitBasis;
        this.shr5_personamartialartstyles = shr5_personamartialartstyles;
    }

    public String getModmanager() {
        return modManager;
    }

    public void setModmanager(String modManager) {
        this.modManager = modManager;
    }
    public int getLogikbasis() {
        return logikBasis;
    }

    public void setLogikbasis(int logikBasis) {
        this.logikBasis = logikBasis;
    }
    public int getWillenskraftbasis() {
        return willenskraftBasis;
    }

    public void setWillenskraftbasis(int willenskraftBasis) {
        this.willenskraftBasis = willenskraftBasis;
    }
    public int getStaerkebasis() {
        return staerkeBasis;
    }

    public void setStaerkebasis(int staerkeBasis) {
        this.staerkeBasis = staerkeBasis;
    }
    public int getCharismabasis() {
        return charismaBasis;
    }

    public void setCharismabasis(int charismaBasis) {
        this.charismaBasis = charismaBasis;
    }
    public int getReaktionbasis() {
        return reaktionBasis;
    }

    public void setReaktionbasis(int reaktionBasis) {
        this.reaktionBasis = reaktionBasis;
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

    public shr5_Spezies getShr5_spezies() {
        return shr5_spezies;
    }

    public void setShr5_spezies(shr5_Spezies shr5_spezies) {
        this.shr5_spezies = shr5_spezies;
    }
    public List<shr5_PersonaMartialartStyle> getShr5_personamartialartstyles() {
        return shr5_personamartialartstyles;
    }

    public void addShr5_personamartialartstyle(Shr5_personamartialartstyle shr5_personamartialartstyle) {
        this.shr5_personamartialartstyles.add(shr5_personamartialartstyle);
    }

}