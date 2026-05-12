





import java.util.List;
import java.util.ArrayList;

public class relational_Index extends RelationalEntity {

    private boolean nullable;
    private boolean autoUpdate;
    private boolean unique;
    private String filterCondition;





    private List<relational_Column> relational_columns;




    private relational_Schema relational_schema;




    private relational_Catalog relational_catalog;




    private relational_Catalog relational_catalog;




    private relational_Schema relational_schema;




    private relational_Column relational_column;


    public relational_Index(
        boolean nullable,        boolean autoUpdate,        boolean unique,        String filterCondition    ) {
        super(
        );
        this.nullable = nullable;
        this.autoUpdate = autoUpdate;
        this.unique = unique;
        this.filterCondition = filterCondition;
        this.relational_columns = new ArrayList<>();
    }

    public relational_Index(
        boolean nullable,        boolean autoUpdate,        boolean unique,        String filterCondition        ArrayList<relational_Column> relational_columns    ) {
        this.nullable = nullable;
        this.autoUpdate = autoUpdate;
        this.unique = unique;
        this.filterCondition = filterCondition;
        this.relational_columns = relational_columns;
    }

    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }
    public boolean getAutoupdate() {
        return autoUpdate;
    }

    public void setAutoupdate(boolean autoUpdate) {
        this.autoUpdate = autoUpdate;
    }
    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }
    public String getFiltercondition() {
        return filterCondition;
    }

    public void setFiltercondition(String filterCondition) {
        this.filterCondition = filterCondition;
    }

    public List<relational_Column> getRelational_columns() {
        return relational_columns;
    }

    public void addRelational_column(Relational_column relational_column) {
        this.relational_columns.add(relational_column);
    }
    public relational_Schema getRelational_schema() {
        return relational_schema;
    }

    public void setRelational_schema(relational_Schema relational_schema) {
        this.relational_schema = relational_schema;
    }
    public relational_Catalog getRelational_catalog() {
        return relational_catalog;
    }

    public void setRelational_catalog(relational_Catalog relational_catalog) {
        this.relational_catalog = relational_catalog;
    }
    public relational_Catalog getRelational_catalog() {
        return relational_catalog;
    }

    public void setRelational_catalog(relational_Catalog relational_catalog) {
        this.relational_catalog = relational_catalog;
    }
    public relational_Schema getRelational_schema() {
        return relational_schema;
    }

    public void setRelational_schema(relational_Schema relational_schema) {
        this.relational_schema = relational_schema;
    }
    public relational_Column getRelational_column() {
        return relational_column;
    }

    public void setRelational_column(relational_Column relational_column) {
        this.relational_column = relational_column;
    }

}