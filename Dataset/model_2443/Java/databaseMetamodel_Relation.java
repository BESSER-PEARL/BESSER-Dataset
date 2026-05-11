





import java.util.List;
import java.util.ArrayList;

public class databaseMetamodel_Relation  {

    private boolean isSelfJoinTable;
    private boolean isJoinTable;
    private String name;





    private databaseMetamodel_Column databasemetamodel_column;




    private List<databaseMetamodel_Column> databasemetamodel_columns;




    private databaseMetamodel_Database databasemetamodel_database;




    private List<databaseMetamodel_Relation> databasemetamodel_relations;




    private List<databaseMetamodel_Column> databasemetamodel_columns;




    private List<databaseMetamodel_Column> databasemetamodel_columns;


    public databaseMetamodel_Relation(
        boolean isSelfJoinTable,        boolean isJoinTable,        String name    ) {
        this.isSelfJoinTable = isSelfJoinTable;
        this.isJoinTable = isJoinTable;
        this.name = name;
        this.databasemetamodel_columns = new ArrayList<>();
        this.databasemetamodel_relations = new ArrayList<>();
        this.databasemetamodel_columns = new ArrayList<>();
        this.databasemetamodel_columns = new ArrayList<>();
    }

    public databaseMetamodel_Relation(
        boolean isSelfJoinTable,        boolean isJoinTable,        String name        ArrayList<databaseMetamodel_Column> databasemetamodel_columns,        ArrayList<databaseMetamodel_Relation> databasemetamodel_relations,        ArrayList<databaseMetamodel_Column> databasemetamodel_columns,        ArrayList<databaseMetamodel_Column> databasemetamodel_columns    ) {
        this.isSelfJoinTable = isSelfJoinTable;
        this.isJoinTable = isJoinTable;
        this.name = name;
        this.databasemetamodel_columns = databasemetamodel_columns;
        this.databasemetamodel_relations = databasemetamodel_relations;
        this.databasemetamodel_columns = databasemetamodel_columns;
        this.databasemetamodel_columns = databasemetamodel_columns;
    }

    public boolean getIsselfjointable() {
        return isSelfJoinTable;
    }

    public void setIsselfjointable(boolean isSelfJoinTable) {
        this.isSelfJoinTable = isSelfJoinTable;
    }
    public boolean getIsjointable() {
        return isJoinTable;
    }

    public void setIsjointable(boolean isJoinTable) {
        this.isJoinTable = isJoinTable;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public databaseMetamodel_Column getDatabasemetamodel_column() {
        return databasemetamodel_column;
    }

    public void setDatabasemetamodel_column(databaseMetamodel_Column databasemetamodel_column) {
        this.databasemetamodel_column = databasemetamodel_column;
    }
    public List<databaseMetamodel_Column> getDatabasemetamodel_columns() {
        return databasemetamodel_columns;
    }

    public void addDatabasemetamodel_column(Databasemetamodel_column databasemetamodel_column) {
        this.databasemetamodel_columns.add(databasemetamodel_column);
    }
    public databaseMetamodel_Database getDatabasemetamodel_database() {
        return databasemetamodel_database;
    }

    public void setDatabasemetamodel_database(databaseMetamodel_Database databasemetamodel_database) {
        this.databasemetamodel_database = databasemetamodel_database;
    }
    public List<databaseMetamodel_Relation> getDatabasemetamodel_relations() {
        return databasemetamodel_relations;
    }

    public void addDatabasemetamodel_relation(Databasemetamodel_relation databasemetamodel_relation) {
        this.databasemetamodel_relations.add(databasemetamodel_relation);
    }
    public List<databaseMetamodel_Column> getDatabasemetamodel_columns() {
        return databasemetamodel_columns;
    }

    public void addDatabasemetamodel_column(Databasemetamodel_column databasemetamodel_column) {
        this.databasemetamodel_columns.add(databasemetamodel_column);
    }
    public List<databaseMetamodel_Column> getDatabasemetamodel_columns() {
        return databasemetamodel_columns;
    }

    public void addDatabasemetamodel_column(Databasemetamodel_column databasemetamodel_column) {
        this.databasemetamodel_columns.add(databasemetamodel_column);
    }

}