





import java.util.List;
import java.util.ArrayList;

public class sipme_Workstation extends EnterpriseProcessor {

    private String ProfileDeescription;





    private sipme_CompanyMember sipme_companymember;




    private sipme_OrganisationCell sipme_organisationcell;




    private List<sipme_CompanyMember> sipme_companymembers;




    private sipme_OrganisationCell sipme_organisationcell;




    private sipme_CompanyMember sipme_companymember;




    private sipme_CompanyMember sipme_companymember;


    public sipme_Workstation(
        String ProfileDeescription    ) {
        super(
        );
        this.ProfileDeescription = ProfileDeescription;
        this.sipme_companymembers = new ArrayList<>();
    }

    public sipme_Workstation(
        String ProfileDeescription        ArrayList<sipme_CompanyMember> sipme_companymembers    ) {
        this.ProfileDeescription = ProfileDeescription;
        this.sipme_companymembers = sipme_companymembers;
    }

    public String getProfiledeescription() {
        return ProfileDeescription;
    }

    public void setProfiledeescription(String ProfileDeescription) {
        this.ProfileDeescription = ProfileDeescription;
    }

    public sipme_CompanyMember getSipme_companymember() {
        return sipme_companymember;
    }

    public void setSipme_companymember(sipme_CompanyMember sipme_companymember) {
        this.sipme_companymember = sipme_companymember;
    }
    public sipme_OrganisationCell getSipme_organisationcell() {
        return sipme_organisationcell;
    }

    public void setSipme_organisationcell(sipme_OrganisationCell sipme_organisationcell) {
        this.sipme_organisationcell = sipme_organisationcell;
    }
    public List<sipme_CompanyMember> getSipme_companymembers() {
        return sipme_companymembers;
    }

    public void addSipme_companymember(Sipme_companymember sipme_companymember) {
        this.sipme_companymembers.add(sipme_companymember);
    }
    public sipme_OrganisationCell getSipme_organisationcell() {
        return sipme_organisationcell;
    }

    public void setSipme_organisationcell(sipme_OrganisationCell sipme_organisationcell) {
        this.sipme_organisationcell = sipme_organisationcell;
    }
    public sipme_CompanyMember getSipme_companymember() {
        return sipme_companymember;
    }

    public void setSipme_companymember(sipme_CompanyMember sipme_companymember) {
        this.sipme_companymember = sipme_companymember;
    }
    public sipme_CompanyMember getSipme_companymember() {
        return sipme_companymember;
    }

    public void setSipme_companymember(sipme_CompanyMember sipme_companymember) {
        this.sipme_companymember = sipme_companymember;
    }

}