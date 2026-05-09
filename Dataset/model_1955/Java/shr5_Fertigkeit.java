





import java.util.List;
import java.util.ArrayList;

public class shr5_Fertigkeit extends Quelle, Beschreibbar, Modifyable {

    private String kategorie;
    private boolean ausweichen;





    private List<shr5_Spezialisierung> shr5_spezialisierungs;




    private shr5_Anwendbar shr5_anwendbar;




    private shr5_Spezialisierung shr5_spezialisierung;




    private shr5_SkillSoft shr5_skillsoft;




    private shr5_AutoSoft shr5_autosoft;




    private shr5_FertigkeitsGruppe shr5_fertigkeitsgruppe;




    private shr5_MartialartStyle shr5_martialartstyle;




    private shr5_Tutorsoft shr5_tutorsoft;




    private shr5_StufenPersona shr5_stufenpersona;


    public shr5_Fertigkeit(
        String kategorie,        boolean ausweichen    ) {
        super(
        );
        this.kategorie = kategorie;
        this.ausweichen = ausweichen;
        this.shr5_spezialisierungs = new ArrayList<>();
    }

    public shr5_Fertigkeit(
        String kategorie,        boolean ausweichen        ArrayList<shr5_Spezialisierung> shr5_spezialisierungs    ) {
        this.kategorie = kategorie;
        this.ausweichen = ausweichen;
        this.shr5_spezialisierungs = shr5_spezialisierungs;
    }

    public String getKategorie() {
        return kategorie;
    }

    public void setKategorie(String kategorie) {
        this.kategorie = kategorie;
    }
    public boolean getAusweichen() {
        return ausweichen;
    }

    public void setAusweichen(boolean ausweichen) {
        this.ausweichen = ausweichen;
    }

    public List<shr5_Spezialisierung> getShr5_spezialisierungs() {
        return shr5_spezialisierungs;
    }

    public void addShr5_spezialisierung(Shr5_spezialisierung shr5_spezialisierung) {
        this.shr5_spezialisierungs.add(shr5_spezialisierung);
    }
    public shr5_Anwendbar getShr5_anwendbar() {
        return shr5_anwendbar;
    }

    public void setShr5_anwendbar(shr5_Anwendbar shr5_anwendbar) {
        this.shr5_anwendbar = shr5_anwendbar;
    }
    public shr5_Spezialisierung getShr5_spezialisierung() {
        return shr5_spezialisierung;
    }

    public void setShr5_spezialisierung(shr5_Spezialisierung shr5_spezialisierung) {
        this.shr5_spezialisierung = shr5_spezialisierung;
    }
    public shr5_SkillSoft getShr5_skillsoft() {
        return shr5_skillsoft;
    }

    public void setShr5_skillsoft(shr5_SkillSoft shr5_skillsoft) {
        this.shr5_skillsoft = shr5_skillsoft;
    }
    public shr5_AutoSoft getShr5_autosoft() {
        return shr5_autosoft;
    }

    public void setShr5_autosoft(shr5_AutoSoft shr5_autosoft) {
        this.shr5_autosoft = shr5_autosoft;
    }
    public shr5_FertigkeitsGruppe getShr5_fertigkeitsgruppe() {
        return shr5_fertigkeitsgruppe;
    }

    public void setShr5_fertigkeitsgruppe(shr5_FertigkeitsGruppe shr5_fertigkeitsgruppe) {
        this.shr5_fertigkeitsgruppe = shr5_fertigkeitsgruppe;
    }
    public shr5_MartialartStyle getShr5_martialartstyle() {
        return shr5_martialartstyle;
    }

    public void setShr5_martialartstyle(shr5_MartialartStyle shr5_martialartstyle) {
        this.shr5_martialartstyle = shr5_martialartstyle;
    }
    public shr5_Tutorsoft getShr5_tutorsoft() {
        return shr5_tutorsoft;
    }

    public void setShr5_tutorsoft(shr5_Tutorsoft shr5_tutorsoft) {
        this.shr5_tutorsoft = shr5_tutorsoft;
    }
    public shr5_StufenPersona getShr5_stufenpersona() {
        return shr5_stufenpersona;
    }

    public void setShr5_stufenpersona(shr5_StufenPersona shr5_stufenpersona) {
        this.shr5_stufenpersona = shr5_stufenpersona;
    }

}