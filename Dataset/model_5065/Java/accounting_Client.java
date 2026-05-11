





import java.util.List;
import java.util.ArrayList;

public class accounting_Client extends NamedElement {






    private accounting_ClientDatabase accounting_clientdatabase;




    private List<accounting_Project> accounting_projects;




    private accounting_Project accounting_project;


    public accounting_Client(
    ) {
        super(
        );
        this.accounting_projects = new ArrayList<>();
    }

    public accounting_Client(
        ArrayList<accounting_Project> accounting_projects    ) {
        this.accounting_projects = accounting_projects;
    }


    public accounting_ClientDatabase getAccounting_clientdatabase() {
        return accounting_clientdatabase;
    }

    public void setAccounting_clientdatabase(accounting_ClientDatabase accounting_clientdatabase) {
        this.accounting_clientdatabase = accounting_clientdatabase;
    }
    public List<accounting_Project> getAccounting_projects() {
        return accounting_projects;
    }

    public void addAccounting_project(Accounting_project accounting_project) {
        this.accounting_projects.add(accounting_project);
    }
    public accounting_Project getAccounting_project() {
        return accounting_project;
    }

    public void setAccounting_project(accounting_Project accounting_project) {
        this.accounting_project = accounting_project;
    }

}