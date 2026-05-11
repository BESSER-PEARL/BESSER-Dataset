





import java.util.List;
import java.util.ArrayList;

public class database_Index extends NamedElement {

    private int cardinality;
    private String qualifier;
    private boolean unique;
    private String indexType;





    private database_Column database_column;


    public database_Index(
        int cardinality,        String qualifier,        boolean unique,        String indexType    ) {
        super(
        );
        this.cardinality = cardinality;
        this.qualifier = qualifier;
        this.unique = unique;
        this.indexType = indexType;
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

    public database_Column getDatabase_column() {
        return database_column;
    }

    public void setDatabase_column(database_Column database_column) {
        this.database_column = database_column;
    }

}