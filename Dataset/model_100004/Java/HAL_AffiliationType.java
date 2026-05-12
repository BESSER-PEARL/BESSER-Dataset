





import java.util.List;
import java.util.ArrayList;

public class HAL_AffiliationType  {

    private String institution;
    private String prive;
    private String universite;
    private String ecole;



    public HAL_AffiliationType(
        String institution,        String prive,        String universite,        String ecole    ) {
        this.institution = institution;
        this.prive = prive;
        this.universite = universite;
        this.ecole = ecole;
    }


    public String getInstitution() {
        return institution;
    }

    public void setInstitution(String institution) {
        this.institution = institution;
    }
    public String getPrive() {
        return prive;
    }

    public void setPrive(String prive) {
        this.prive = prive;
    }
    public String getUniversite() {
        return universite;
    }

    public void setUniversite(String universite) {
        this.universite = universite;
    }
    public String getEcole() {
        return ecole;
    }

    public void setEcole(String ecole) {
        this.ecole = ecole;
    }


}