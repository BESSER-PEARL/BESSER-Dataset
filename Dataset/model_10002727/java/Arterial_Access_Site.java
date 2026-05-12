





import java.util.List;
import java.util.ArrayList;

public class Arterial_Access_Site  {

    private String CathPCI_Arterial_Access_Site;
    private String Carotid_Intervention_Arterial_Access_Site;
    private String Renal_Arterial_Access_Site;
    private String Lower_Extremity_Arterial_Access_Site;
    private String AAA_Arterial_Access_Site;



    public Arterial_Access_Site(
        String CathPCI_Arterial_Access_Site,        String Carotid_Intervention_Arterial_Access_Site,        String Renal_Arterial_Access_Site,        String Lower_Extremity_Arterial_Access_Site,        String AAA_Arterial_Access_Site    ) {
        this.CathPCI_Arterial_Access_Site = CathPCI_Arterial_Access_Site;
        this.Carotid_Intervention_Arterial_Access_Site = Carotid_Intervention_Arterial_Access_Site;
        this.Renal_Arterial_Access_Site = Renal_Arterial_Access_Site;
        this.Lower_Extremity_Arterial_Access_Site = Lower_Extremity_Arterial_Access_Site;
        this.AAA_Arterial_Access_Site = AAA_Arterial_Access_Site;
    }


    public String getCathpci_arterial_access_site() {
        return CathPCI_Arterial_Access_Site;
    }

    public void setCathpci_arterial_access_site(String CathPCI_Arterial_Access_Site) {
        this.CathPCI_Arterial_Access_Site = CathPCI_Arterial_Access_Site;
    }
    public String getCarotid_intervention_arterial_access_site() {
        return Carotid_Intervention_Arterial_Access_Site;
    }

    public void setCarotid_intervention_arterial_access_site(String Carotid_Intervention_Arterial_Access_Site) {
        this.Carotid_Intervention_Arterial_Access_Site = Carotid_Intervention_Arterial_Access_Site;
    }
    public String getRenal_arterial_access_site() {
        return Renal_Arterial_Access_Site;
    }

    public void setRenal_arterial_access_site(String Renal_Arterial_Access_Site) {
        this.Renal_Arterial_Access_Site = Renal_Arterial_Access_Site;
    }
    public String getLower_extremity_arterial_access_site() {
        return Lower_Extremity_Arterial_Access_Site;
    }

    public void setLower_extremity_arterial_access_site(String Lower_Extremity_Arterial_Access_Site) {
        this.Lower_Extremity_Arterial_Access_Site = Lower_Extremity_Arterial_Access_Site;
    }
    public String getAaa_arterial_access_site() {
        return AAA_Arterial_Access_Site;
    }

    public void setAaa_arterial_access_site(String AAA_Arterial_Access_Site) {
        this.AAA_Arterial_Access_Site = AAA_Arterial_Access_Site;
    }


}