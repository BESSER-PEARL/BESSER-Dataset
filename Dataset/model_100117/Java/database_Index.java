





import java.util.List;
import java.util.ArrayList;

public class database_Index extends NamedElement {

    private int cardinality;
    private boolean unique;
    private String indexType;
    private String qualifier;





    private List<database_IndexElement> database_indexelements;


    public database_Index(
        int cardinality,        boolean unique,        String indexType,        String qualifier    ) {
        super(
        );
        this.cardinality = cardinality;
        this.unique = unique;
        this.indexType = indexType;
        this.qualifier = qualifier;
        this.database_indexelements = new ArrayList<>();
    }

    public database_Index(
        int cardinality,        boolean unique,        String indexType,        String qualifier        ArrayList<database_IndexElement> database_indexelements    ) {
        this.cardinality = cardinality;
        this.unique = unique;
        this.indexType = indexType;
        this.qualifier = qualifier;
        this.database_indexelements = database_indexelements;
    }

    public int getCardinality() {
        return cardinality;
    }

    public void setCardinality(int cardinality) {
        this.cardinality = cardinality;
    }
    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
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

    public List<database_IndexElement> getDatabase_indexelements() {
        return database_indexelements;
    }

    public void addDatabase_indexelement(Database_indexelement database_indexelement) {
        this.database_indexelements.add(database_indexelement);
    }

}