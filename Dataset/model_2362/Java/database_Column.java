





import java.util.List;
import java.util.ArrayList;

public class database_Column extends NamedElement {

    private boolean unique;
    private boolean nullable;
    private boolean inPrimaryKey;
    private boolean autoincrement;
    private boolean inForeignKey;
    private String defaultValue;





    private List<database_IndexElement> database_indexelements;




    private database_IndexElement database_indexelement;




    private database_PrimaryKey database_primarykey;




    private database_Type database_type;




    private List<database_ForeignKeyElement> database_foreignkeyelements;




    private List<database_ForeignKey> database_foreignkeys;




    private List<database_Index> database_indexs;




    private database_AbstractTable database_abstracttable;




    private database_ForeignKeyElement database_foreignkeyelement;




    private database_AbstractTable database_abstracttable;




    private database_ForeignKeyElement database_foreignkeyelement;




    private database_Sequence database_sequence;




    private database_PrimaryKey database_primarykey;


    public database_Column(
        boolean unique,        boolean nullable,        boolean inPrimaryKey,        boolean autoincrement,        boolean inForeignKey,        String defaultValue    ) {
        super(
        );
        this.unique = unique;
        this.nullable = nullable;
        this.inPrimaryKey = inPrimaryKey;
        this.autoincrement = autoincrement;
        this.inForeignKey = inForeignKey;
        this.defaultValue = defaultValue;
        this.database_indexelements = new ArrayList<>();
        this.database_foreignkeyelements = new ArrayList<>();
        this.database_foreignkeys = new ArrayList<>();
        this.database_indexs = new ArrayList<>();
    }

    public database_Column(
        boolean unique,        boolean nullable,        boolean inPrimaryKey,        boolean autoincrement,        boolean inForeignKey,        String defaultValue        ArrayList<database_IndexElement> database_indexelements,        ArrayList<database_ForeignKeyElement> database_foreignkeyelements,        ArrayList<database_ForeignKey> database_foreignkeys,        ArrayList<database_Index> database_indexs    ) {
        this.unique = unique;
        this.nullable = nullable;
        this.inPrimaryKey = inPrimaryKey;
        this.autoincrement = autoincrement;
        this.inForeignKey = inForeignKey;
        this.defaultValue = defaultValue;
        this.database_indexelements = database_indexelements;
        this.database_foreignkeyelements = database_foreignkeyelements;
        this.database_foreignkeys = database_foreignkeys;
        this.database_indexs = database_indexs;
    }

    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }
    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }
    public boolean getInprimarykey() {
        return inPrimaryKey;
    }

    public void setInprimarykey(boolean inPrimaryKey) {
        this.inPrimaryKey = inPrimaryKey;
    }
    public boolean getAutoincrement() {
        return autoincrement;
    }

    public void setAutoincrement(boolean autoincrement) {
        this.autoincrement = autoincrement;
    }
    public boolean getInforeignkey() {
        return inForeignKey;
    }

    public void setInforeignkey(boolean inForeignKey) {
        this.inForeignKey = inForeignKey;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }

    public List<database_IndexElement> getDatabase_indexelements() {
        return database_indexelements;
    }

    public void addDatabase_indexelement(Database_indexelement database_indexelement) {
        this.database_indexelements.add(database_indexelement);
    }
    public database_IndexElement getDatabase_indexelement() {
        return database_indexelement;
    }

    public void setDatabase_indexelement(database_IndexElement database_indexelement) {
        this.database_indexelement = database_indexelement;
    }
    public database_PrimaryKey getDatabase_primarykey() {
        return database_primarykey;
    }

    public void setDatabase_primarykey(database_PrimaryKey database_primarykey) {
        this.database_primarykey = database_primarykey;
    }
    public database_Type getDatabase_type() {
        return database_type;
    }

    public void setDatabase_type(database_Type database_type) {
        this.database_type = database_type;
    }
    public List<database_ForeignKeyElement> getDatabase_foreignkeyelements() {
        return database_foreignkeyelements;
    }

    public void addDatabase_foreignkeyelement(Database_foreignkeyelement database_foreignkeyelement) {
        this.database_foreignkeyelements.add(database_foreignkeyelement);
    }
    public List<database_ForeignKey> getDatabase_foreignkeys() {
        return database_foreignkeys;
    }

    public void addDatabase_foreignkey(Database_foreignkey database_foreignkey) {
        this.database_foreignkeys.add(database_foreignkey);
    }
    public List<database_Index> getDatabase_indexs() {
        return database_indexs;
    }

    public void addDatabase_index(Database_index database_index) {
        this.database_indexs.add(database_index);
    }
    public database_AbstractTable getDatabase_abstracttable() {
        return database_abstracttable;
    }

    public void setDatabase_abstracttable(database_AbstractTable database_abstracttable) {
        this.database_abstracttable = database_abstracttable;
    }
    public database_ForeignKeyElement getDatabase_foreignkeyelement() {
        return database_foreignkeyelement;
    }

    public void setDatabase_foreignkeyelement(database_ForeignKeyElement database_foreignkeyelement) {
        this.database_foreignkeyelement = database_foreignkeyelement;
    }
    public database_AbstractTable getDatabase_abstracttable() {
        return database_abstracttable;
    }

    public void setDatabase_abstracttable(database_AbstractTable database_abstracttable) {
        this.database_abstracttable = database_abstracttable;
    }
    public database_ForeignKeyElement getDatabase_foreignkeyelement() {
        return database_foreignkeyelement;
    }

    public void setDatabase_foreignkeyelement(database_ForeignKeyElement database_foreignkeyelement) {
        this.database_foreignkeyelement = database_foreignkeyelement;
    }
    public database_Sequence getDatabase_sequence() {
        return database_sequence;
    }

    public void setDatabase_sequence(database_Sequence database_sequence) {
        this.database_sequence = database_sequence;
    }
    public database_PrimaryKey getDatabase_primarykey() {
        return database_primarykey;
    }

    public void setDatabase_primarykey(database_PrimaryKey database_primarykey) {
        this.database_primarykey = database_primarykey;
    }

}