





import java.util.List;
import java.util.ArrayList;

public class project_Account extends Property, AccountAttribute {

    private String id;
    private String name;





    private project_AccountShare project_accountshare;




    private project_Balance project_balance;




    private project_Balance project_balance;


    public project_Account(
        String id,        String name    ) {
        super(
        );
        this.id = id;
        this.name = name;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public project_AccountShare getProject_accountshare() {
        return project_accountshare;
    }

    public void setProject_accountshare(project_AccountShare project_accountshare) {
        this.project_accountshare = project_accountshare;
    }
    public project_Balance getProject_balance() {
        return project_balance;
    }

    public void setProject_balance(project_Balance project_balance) {
        this.project_balance = project_balance;
    }
    public project_Balance getProject_balance() {
        return project_balance;
    }

    public void setProject_balance(project_Balance project_balance) {
        this.project_balance = project_balance;
    }

}