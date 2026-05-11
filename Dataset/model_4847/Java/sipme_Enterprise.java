





import java.util.List;
import java.util.ArrayList;

public class sipme_Enterprise extends EnterpriseProcessor {

    private String status;
    private String acronym;





    private List<sipme_Domain> sipme_domains;




    private List<sipme_CompanyMember> sipme_companymembers;




    private List<sipme_EnterpriseProduct> sipme_enterpriseproducts;




    private List<sipme_EnterpriseService> sipme_enterpriseservices;




    private List<sipme_EnterpriseObject> sipme_enterpriseobjects;




    private List<sipme_OrganisationCell> sipme_organisationcells;




    private List<sipme_Objective> sipme_objectives;


    public sipme_Enterprise(
        String status,        String acronym    ) {
        super(
        );
        this.status = status;
        this.acronym = acronym;
        this.sipme_domains = new ArrayList<>();
        this.sipme_companymembers = new ArrayList<>();
        this.sipme_enterpriseproducts = new ArrayList<>();
        this.sipme_enterpriseservices = new ArrayList<>();
        this.sipme_enterpriseobjects = new ArrayList<>();
        this.sipme_organisationcells = new ArrayList<>();
        this.sipme_objectives = new ArrayList<>();
    }

    public sipme_Enterprise(
        String status,        String acronym        ArrayList<sipme_Domain> sipme_domains,        ArrayList<sipme_CompanyMember> sipme_companymembers,        ArrayList<sipme_EnterpriseProduct> sipme_enterpriseproducts,        ArrayList<sipme_EnterpriseService> sipme_enterpriseservices,        ArrayList<sipme_EnterpriseObject> sipme_enterpriseobjects,        ArrayList<sipme_OrganisationCell> sipme_organisationcells,        ArrayList<sipme_Objective> sipme_objectives    ) {
        this.status = status;
        this.acronym = acronym;
        this.sipme_domains = sipme_domains;
        this.sipme_companymembers = sipme_companymembers;
        this.sipme_enterpriseproducts = sipme_enterpriseproducts;
        this.sipme_enterpriseservices = sipme_enterpriseservices;
        this.sipme_enterpriseobjects = sipme_enterpriseobjects;
        this.sipme_organisationcells = sipme_organisationcells;
        this.sipme_objectives = sipme_objectives;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getAcronym() {
        return acronym;
    }

    public void setAcronym(String acronym) {
        this.acronym = acronym;
    }

    public List<sipme_Domain> getSipme_domains() {
        return sipme_domains;
    }

    public void addSipme_domain(Sipme_domain sipme_domain) {
        this.sipme_domains.add(sipme_domain);
    }
    public List<sipme_CompanyMember> getSipme_companymembers() {
        return sipme_companymembers;
    }

    public void addSipme_companymember(Sipme_companymember sipme_companymember) {
        this.sipme_companymembers.add(sipme_companymember);
    }
    public List<sipme_EnterpriseProduct> getSipme_enterpriseproducts() {
        return sipme_enterpriseproducts;
    }

    public void addSipme_enterpriseproduct(Sipme_enterpriseproduct sipme_enterpriseproduct) {
        this.sipme_enterpriseproducts.add(sipme_enterpriseproduct);
    }
    public List<sipme_EnterpriseService> getSipme_enterpriseservices() {
        return sipme_enterpriseservices;
    }

    public void addSipme_enterpriseservice(Sipme_enterpriseservice sipme_enterpriseservice) {
        this.sipme_enterpriseservices.add(sipme_enterpriseservice);
    }
    public List<sipme_EnterpriseObject> getSipme_enterpriseobjects() {
        return sipme_enterpriseobjects;
    }

    public void addSipme_enterpriseobject(Sipme_enterpriseobject sipme_enterpriseobject) {
        this.sipme_enterpriseobjects.add(sipme_enterpriseobject);
    }
    public List<sipme_OrganisationCell> getSipme_organisationcells() {
        return sipme_organisationcells;
    }

    public void addSipme_organisationcell(Sipme_organisationcell sipme_organisationcell) {
        this.sipme_organisationcells.add(sipme_organisationcell);
    }
    public List<sipme_Objective> getSipme_objectives() {
        return sipme_objectives;
    }

    public void addSipme_objective(Sipme_objective sipme_objective) {
        this.sipme_objectives.add(sipme_objective);
    }

}