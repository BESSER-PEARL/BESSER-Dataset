





import java.util.List;
import java.util.ArrayList;

public class dbca_Server extends NamedElement {






    private List<dbca_ServerElement> dbca_serverelements;




    private dbca_Application dbca_application;


    public dbca_Server(
    ) {
        super(
        );
        this.dbca_serverelements = new ArrayList<>();
    }

    public dbca_Server(
        ArrayList<dbca_ServerElement> dbca_serverelements    ) {
        this.dbca_serverelements = dbca_serverelements;
    }


    public List<dbca_ServerElement> getDbca_serverelements() {
        return dbca_serverelements;
    }

    public void addDbca_serverelement(Dbca_serverelement dbca_serverelement) {
        this.dbca_serverelements.add(dbca_serverelement);
    }
    public dbca_Application getDbca_application() {
        return dbca_application;
    }

    public void setDbca_application(dbca_Application dbca_application) {
        this.dbca_application = dbca_application;
    }

}