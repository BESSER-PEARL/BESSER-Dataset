





import java.util.List;
import java.util.ArrayList;

public class dbmddandroid_Table extends NamedElement {






    private List<dbmddandroid_Relation> dbmddandroid_relations;




    private List<dbmddandroid_Relation> dbmddandroid_relations;




    private List<dbmddandroid_Column> dbmddandroid_columns;




    private dbmddandroid_DBScheme dbmddandroid_dbscheme;




    private dbmddandroid_Relation dbmddandroid_relation;




    private dbmddandroid_Relation dbmddandroid_relation;


    public dbmddandroid_Table(
    ) {
        super(
        );
        this.dbmddandroid_relations = new ArrayList<>();
        this.dbmddandroid_relations = new ArrayList<>();
        this.dbmddandroid_columns = new ArrayList<>();
    }

    public dbmddandroid_Table(
        ArrayList<dbmddandroid_Relation> dbmddandroid_relations,        ArrayList<dbmddandroid_Relation> dbmddandroid_relations,        ArrayList<dbmddandroid_Column> dbmddandroid_columns    ) {
        this.dbmddandroid_relations = dbmddandroid_relations;
        this.dbmddandroid_relations = dbmddandroid_relations;
        this.dbmddandroid_columns = dbmddandroid_columns;
    }


    public List<dbmddandroid_Relation> getDbmddandroid_relations() {
        return dbmddandroid_relations;
    }

    public void addDbmddandroid_relation(Dbmddandroid_relation dbmddandroid_relation) {
        this.dbmddandroid_relations.add(dbmddandroid_relation);
    }
    public List<dbmddandroid_Relation> getDbmddandroid_relations() {
        return dbmddandroid_relations;
    }

    public void addDbmddandroid_relation(Dbmddandroid_relation dbmddandroid_relation) {
        this.dbmddandroid_relations.add(dbmddandroid_relation);
    }
    public List<dbmddandroid_Column> getDbmddandroid_columns() {
        return dbmddandroid_columns;
    }

    public void addDbmddandroid_column(Dbmddandroid_column dbmddandroid_column) {
        this.dbmddandroid_columns.add(dbmddandroid_column);
    }
    public dbmddandroid_DBScheme getDbmddandroid_dbscheme() {
        return dbmddandroid_dbscheme;
    }

    public void setDbmddandroid_dbscheme(dbmddandroid_DBScheme dbmddandroid_dbscheme) {
        this.dbmddandroid_dbscheme = dbmddandroid_dbscheme;
    }
    public dbmddandroid_Relation getDbmddandroid_relation() {
        return dbmddandroid_relation;
    }

    public void setDbmddandroid_relation(dbmddandroid_Relation dbmddandroid_relation) {
        this.dbmddandroid_relation = dbmddandroid_relation;
    }
    public dbmddandroid_Relation getDbmddandroid_relation() {
        return dbmddandroid_relation;
    }

    public void setDbmddandroid_relation(dbmddandroid_Relation dbmddandroid_relation) {
        this.dbmddandroid_relation = dbmddandroid_relation;
    }

}