





import java.util.List;
import java.util.ArrayList;

public class sipme_OrganisationCell extends EnterpriseProcessor {

    private int organisationLevel;





    private List<sipme_Domain> sipme_domains;




    private sipme_Domain sipme_domain;




    private sipme_CompanyMember sipme_companymember;




    private sipme_CompanyMember sipme_companymember;




    private List<sipme_OrganisationCell> sipme_organisationcells;


    public sipme_OrganisationCell(
        int organisationLevel    ) {
        super(
        );
        this.organisationLevel = organisationLevel;
        this.sipme_domains = new ArrayList<>();
        this.sipme_organisationcells = new ArrayList<>();
    }

    public sipme_OrganisationCell(
        int organisationLevel        ArrayList<sipme_Domain> sipme_domains,        ArrayList<sipme_OrganisationCell> sipme_organisationcells    ) {
        this.organisationLevel = organisationLevel;
        this.sipme_domains = sipme_domains;
        this.sipme_organisationcells = sipme_organisationcells;
    }

    public int getOrganisationlevel() {
        return organisationLevel;
    }

    public void setOrganisationlevel(int organisationLevel) {
        this.organisationLevel = organisationLevel;
    }

    public List<sipme_Domain> getSipme_domains() {
        return sipme_domains;
    }

    public void addSipme_domain(Sipme_domain sipme_domain) {
        this.sipme_domains.add(sipme_domain);
    }
    public sipme_Domain getSipme_domain() {
        return sipme_domain;
    }

    public void setSipme_domain(sipme_Domain sipme_domain) {
        this.sipme_domain = sipme_domain;
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
    public List<sipme_OrganisationCell> getSipme_organisationcells() {
        return sipme_organisationcells;
    }

    public void addSipme_organisationcell(Sipme_organisationcell sipme_organisationcell) {
        this.sipme_organisationcells.add(sipme_organisationcell);
    }

}