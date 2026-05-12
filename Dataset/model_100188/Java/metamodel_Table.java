





import java.util.List;
import java.util.ArrayList;

public class metamodel_Table  {

    private String name;





    private metamodel_Database metamodel_database;




    private List<metamodel_Row> metamodel_rows;




    private List<metamodel_Constraint> metamodel_constraints;




    private List<metamodel_Column> metamodel_columns;


    public metamodel_Table(
        String name    ) {
        this.name = name;
        this.metamodel_rows = new ArrayList<>();
        this.metamodel_constraints = new ArrayList<>();
        this.metamodel_columns = new ArrayList<>();
    }

    public metamodel_Table(
        String name        ArrayList<metamodel_Row> metamodel_rows,        ArrayList<metamodel_Constraint> metamodel_constraints,        ArrayList<metamodel_Column> metamodel_columns    ) {
        this.name = name;
        this.metamodel_rows = metamodel_rows;
        this.metamodel_constraints = metamodel_constraints;
        this.metamodel_columns = metamodel_columns;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public metamodel_Database getMetamodel_database() {
        return metamodel_database;
    }

    public void setMetamodel_database(metamodel_Database metamodel_database) {
        this.metamodel_database = metamodel_database;
    }
    public List<metamodel_Row> getMetamodel_rows() {
        return metamodel_rows;
    }

    public void addMetamodel_row(Metamodel_row metamodel_row) {
        this.metamodel_rows.add(metamodel_row);
    }
    public List<metamodel_Constraint> getMetamodel_constraints() {
        return metamodel_constraints;
    }

    public void addMetamodel_constraint(Metamodel_constraint metamodel_constraint) {
        this.metamodel_constraints.add(metamodel_constraint);
    }
    public List<metamodel_Column> getMetamodel_columns() {
        return metamodel_columns;
    }

    public void addMetamodel_column(Metamodel_column metamodel_column) {
        this.metamodel_columns.add(metamodel_column);
    }

}