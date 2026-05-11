





import java.util.List;
import java.util.ArrayList;

public class fds_Table extends NamedElement {






    private List<fds_FunctionalDependency> fds_functionaldependencys;




    private fds_Database fds_database;




    private List<fds_Restriction> fds_restrictions;




    private List<fds_Column> fds_columns;


    public fds_Table(
    ) {
        super(
        );
        this.fds_functionaldependencys = new ArrayList<>();
        this.fds_restrictions = new ArrayList<>();
        this.fds_columns = new ArrayList<>();
    }

    public fds_Table(
        ArrayList<fds_FunctionalDependency> fds_functionaldependencys,        ArrayList<fds_Restriction> fds_restrictions,        ArrayList<fds_Column> fds_columns    ) {
        this.fds_functionaldependencys = fds_functionaldependencys;
        this.fds_restrictions = fds_restrictions;
        this.fds_columns = fds_columns;
    }


    public List<fds_FunctionalDependency> getFds_functionaldependencys() {
        return fds_functionaldependencys;
    }

    public void addFds_functionaldependency(Fds_functionaldependency fds_functionaldependency) {
        this.fds_functionaldependencys.add(fds_functionaldependency);
    }
    public fds_Database getFds_database() {
        return fds_database;
    }

    public void setFds_database(fds_Database fds_database) {
        this.fds_database = fds_database;
    }
    public List<fds_Restriction> getFds_restrictions() {
        return fds_restrictions;
    }

    public void addFds_restriction(Fds_restriction fds_restriction) {
        this.fds_restrictions.add(fds_restriction);
    }
    public List<fds_Column> getFds_columns() {
        return fds_columns;
    }

    public void addFds_column(Fds_column fds_column) {
        this.fds_columns.add(fds_column);
    }

}