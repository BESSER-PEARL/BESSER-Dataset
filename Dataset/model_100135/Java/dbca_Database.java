





import java.util.List;
import java.util.ArrayList;

public class dbca_Database extends NamedElement {






    private List<dbca_DatabaseElement> dbca_databaseelements;




    private dbca_Application dbca_application;


    public dbca_Database(
    ) {
        super(
        );
        this.dbca_databaseelements = new ArrayList<>();
    }

    public dbca_Database(
        ArrayList<dbca_DatabaseElement> dbca_databaseelements    ) {
        this.dbca_databaseelements = dbca_databaseelements;
    }


    public List<dbca_DatabaseElement> getDbca_databaseelements() {
        return dbca_databaseelements;
    }

    public void addDbca_databaseelement(Dbca_databaseelement dbca_databaseelement) {
        this.dbca_databaseelements.add(dbca_databaseelement);
    }
    public dbca_Application getDbca_application() {
        return dbca_application;
    }

    public void setDbca_application(dbca_Application dbca_application) {
        this.dbca_application = dbca_application;
    }

}