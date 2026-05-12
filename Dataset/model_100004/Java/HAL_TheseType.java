





import java.util.List;
import java.util.ArrayList;

public class HAL_TheseType extends ReferenceBiblioType {

    private String codirecteur;
    private String directeur;
    private String niveau;
    private String defencedate;
    private String orgthe;



    public HAL_TheseType(
        String codirecteur,        String directeur,        String niveau,        String defencedate,        String orgthe    ) {
        super(
        );
        this.codirecteur = codirecteur;
        this.directeur = directeur;
        this.niveau = niveau;
        this.defencedate = defencedate;
        this.orgthe = orgthe;
    }


    public String getCodirecteur() {
        return codirecteur;
    }

    public void setCodirecteur(String codirecteur) {
        this.codirecteur = codirecteur;
    }
    public String getDirecteur() {
        return directeur;
    }

    public void setDirecteur(String directeur) {
        this.directeur = directeur;
    }
    public String getNiveau() {
        return niveau;
    }

    public void setNiveau(String niveau) {
        this.niveau = niveau;
    }
    public String getDefencedate() {
        return defencedate;
    }

    public void setDefencedate(String defencedate) {
        this.defencedate = defencedate;
    }
    public String getOrgthe() {
        return orgthe;
    }

    public void setOrgthe(String orgthe) {
        this.orgthe = orgthe;
    }


}