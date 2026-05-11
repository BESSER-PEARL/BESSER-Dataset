





import java.util.List;
import java.util.ArrayList;

public class database_Index extends NamedElement {

    private boolean unique;
    private int cardinality;
    private String qualifier;
    private String indexType;





    private List<database_IndexElement> database_indexelements;


    public database_Index(
        boolean unique,        int cardinality,        String qualifier,        String indexType    ) {
        super(
        );
        this.unique = unique;
        this.cardinality = cardinality;
        this.qualifier = qualifier;
        this.indexType = indexType;
        this.database_indexelements = new ArrayList<>();
    }

    public database_Index(
        boolean unique,        int cardinality,        String qualifier,        String indexType        ArrayList<database_IndexElement> database_indexelements    ) {
        this.unique = unique;
        this.cardinality = cardinality;
        this.qualifier = qualifier;
        this.indexType = indexType;
        this.database_indexelements = database_indexelements;
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
    public String getQualifier() {
        return qualifier;
    }

    public void setQualifier(String qualifier) {
        this.qualifier = qualifier;
    }
    public String getIndextype() {
        return indexType;
    }

    public void setIndextype(String indexType) {
        this.indexType = indexType;
    }

    public List<database_IndexElement> getDatabase_indexelements() {
        return database_indexelements;
    }

    public void addDatabase_indexelement(Database_indexelement database_indexelement) {
        this.database_indexelements.add(database_indexelement);
    }

}