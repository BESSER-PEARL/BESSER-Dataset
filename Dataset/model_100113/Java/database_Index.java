





import java.util.List;
import java.util.ArrayList;

public class database_Index extends NamedElement {

    private String indexType;
    private String qualifier;
    private boolean unique;
    private int cardinality;





    private List<database_IndexElement> database_indexelements;


    public database_Index(
        String indexType,        String qualifier,        boolean unique,        int cardinality    ) {
        super(
        );
        this.indexType = indexType;
        this.qualifier = qualifier;
        this.unique = unique;
        this.cardinality = cardinality;
        this.database_indexelements = new ArrayList<>();
    }

    public database_Index(
        String indexType,        String qualifier,        boolean unique,        int cardinality        ArrayList<database_IndexElement> database_indexelements    ) {
        this.indexType = indexType;
        this.qualifier = qualifier;
        this.unique = unique;
        this.cardinality = cardinality;
        this.database_indexelements = database_indexelements;
    }

    public String getIndextype() {
        return indexType;
    }

    public void setIndextype(String indexType) {
        this.indexType = indexType;
    }
    public String getQualifier() {
        return qualifier;
    }

    public void setQualifier(String qualifier) {
        this.qualifier = qualifier;
    }
    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }
    public int getCardinality() {
        return cardinality;
    }

    public void setCardinality(int cardinality) {
        this.cardinality = cardinality;
    }

    public List<database_IndexElement> getDatabase_indexelements() {
        return database_indexelements;
    }

    public void addDatabase_indexelement(Database_indexelement database_indexelement) {
        this.database_indexelements.add(database_indexelement);
    }

}