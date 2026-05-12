





import java.util.List;
import java.util.ArrayList;

public class publisher  {

    private String OrgContact;
    private String OrgName;
    private int EstablishedYear;
    private String OrgAddress;



    public publisher(
        String OrgContact,        String OrgName,        int EstablishedYear,        String OrgAddress    ) {
        this.OrgContact = OrgContact;
        this.OrgName = OrgName;
        this.EstablishedYear = EstablishedYear;
        this.OrgAddress = OrgAddress;
    }


    public String getOrgcontact() {
        return OrgContact;
    }

    public void setOrgcontact(String OrgContact) {
        this.OrgContact = OrgContact;
    }
    public String getOrgname() {
        return OrgName;
    }

    public void setOrgname(String OrgName) {
        this.OrgName = OrgName;
    }
    public int getEstablishedyear() {
        return EstablishedYear;
    }

    public void setEstablishedyear(int EstablishedYear) {
        this.EstablishedYear = EstablishedYear;
    }
    public String getOrgaddress() {
        return OrgAddress;
    }

    public void setOrgaddress(String OrgAddress) {
        this.OrgAddress = OrgAddress;
    }


}