





import java.util.List;
import java.util.ArrayList;

public class sipme_Role_Function extends EnterpriseProcessor {

    private String roleType;





    private List<sipme_BusinessRules> sipme_businessruless;




    private List<sipme_EnterpriseProcessor> sipme_enterpriseprocessors;




    private List<sipme_Task> sipme_tasks;




    private List<sipme_EnterpriseResource> sipme_enterpriseresources;




    private sipme_EnterpriseResource sipme_enterpriseresource;




    private List<sipme_EnterpriseResource> sipme_enterpriseresources;




    private sipme_EnterpriseProcessor sipme_enterpriseprocessor;




    private sipme_EnterpriseResource sipme_enterpriseresource;


    public sipme_Role_Function(
        String roleType    ) {
        super(
        );
        this.roleType = roleType;
        this.sipme_businessruless = new ArrayList<>();
        this.sipme_enterpriseprocessors = new ArrayList<>();
        this.sipme_tasks = new ArrayList<>();
        this.sipme_enterpriseresources = new ArrayList<>();
        this.sipme_enterpriseresources = new ArrayList<>();
    }

    public sipme_Role_Function(
        String roleType        ArrayList<sipme_BusinessRules> sipme_businessruless,        ArrayList<sipme_EnterpriseProcessor> sipme_enterpriseprocessors,        ArrayList<sipme_Task> sipme_tasks,        ArrayList<sipme_EnterpriseResource> sipme_enterpriseresources,        ArrayList<sipme_EnterpriseResource> sipme_enterpriseresources    ) {
        this.roleType = roleType;
        this.sipme_businessruless = sipme_businessruless;
        this.sipme_enterpriseprocessors = sipme_enterpriseprocessors;
        this.sipme_tasks = sipme_tasks;
        this.sipme_enterpriseresources = sipme_enterpriseresources;
        this.sipme_enterpriseresources = sipme_enterpriseresources;
    }

    public String getRoletype() {
        return roleType;
    }

    public void setRoletype(String roleType) {
        this.roleType = roleType;
    }

    public List<sipme_BusinessRules> getSipme_businessruless() {
        return sipme_businessruless;
    }

    public void addSipme_businessrules(Sipme_businessrules sipme_businessrules) {
        this.sipme_businessruless.add(sipme_businessrules);
    }
    public List<sipme_EnterpriseProcessor> getSipme_enterpriseprocessors() {
        return sipme_enterpriseprocessors;
    }

    public void addSipme_enterpriseprocessor(Sipme_enterpriseprocessor sipme_enterpriseprocessor) {
        this.sipme_enterpriseprocessors.add(sipme_enterpriseprocessor);
    }
    public List<sipme_Task> getSipme_tasks() {
        return sipme_tasks;
    }

    public void addSipme_task(Sipme_task sipme_task) {
        this.sipme_tasks.add(sipme_task);
    }
    public List<sipme_EnterpriseResource> getSipme_enterpriseresources() {
        return sipme_enterpriseresources;
    }

    public void addSipme_enterpriseresource(Sipme_enterpriseresource sipme_enterpriseresource) {
        this.sipme_enterpriseresources.add(sipme_enterpriseresource);
    }
    public sipme_EnterpriseResource getSipme_enterpriseresource() {
        return sipme_enterpriseresource;
    }

    public void setSipme_enterpriseresource(sipme_EnterpriseResource sipme_enterpriseresource) {
        this.sipme_enterpriseresource = sipme_enterpriseresource;
    }
    public List<sipme_EnterpriseResource> getSipme_enterpriseresources() {
        return sipme_enterpriseresources;
    }

    public void addSipme_enterpriseresource(Sipme_enterpriseresource sipme_enterpriseresource) {
        this.sipme_enterpriseresources.add(sipme_enterpriseresource);
    }
    public sipme_EnterpriseProcessor getSipme_enterpriseprocessor() {
        return sipme_enterpriseprocessor;
    }

    public void setSipme_enterpriseprocessor(sipme_EnterpriseProcessor sipme_enterpriseprocessor) {
        this.sipme_enterpriseprocessor = sipme_enterpriseprocessor;
    }
    public sipme_EnterpriseResource getSipme_enterpriseresource() {
        return sipme_enterpriseresource;
    }

    public void setSipme_enterpriseresource(sipme_EnterpriseResource sipme_enterpriseresource) {
        this.sipme_enterpriseresource = sipme_enterpriseresource;
    }

}