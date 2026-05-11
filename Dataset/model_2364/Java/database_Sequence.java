





import java.util.List;
import java.util.ArrayList;

public class database_Sequence extends NamedElement {

    private String cacheSize;
    private String minValue;
    private boolean cycle;
    private String increment;
    private String maxValue;
    private String start;





    private database_Column database_column;




    private List<database_Column> database_columns;




    private database_TableContainer database_tablecontainer;


    public database_Sequence(
        String cacheSize,        String minValue,        boolean cycle,        String increment,        String maxValue,        String start    ) {
        super(
        );
        this.cacheSize = cacheSize;
        this.minValue = minValue;
        this.cycle = cycle;
        this.increment = increment;
        this.maxValue = maxValue;
        this.start = start;
        this.database_columns = new ArrayList<>();
    }

    public database_Sequence(
        String cacheSize,        String minValue,        boolean cycle,        String increment,        String maxValue,        String start        ArrayList<database_Column> database_columns    ) {
        this.cacheSize = cacheSize;
        this.minValue = minValue;
        this.cycle = cycle;
        this.increment = increment;
        this.maxValue = maxValue;
        this.start = start;
        this.database_columns = database_columns;
    }

    public String getCachesize() {
        return cacheSize;
    }

    public void setCachesize(String cacheSize) {
        this.cacheSize = cacheSize;
    }
    public String getMinvalue() {
        return minValue;
    }

    public void setMinvalue(String minValue) {
        this.minValue = minValue;
    }
    public boolean getCycle() {
        return cycle;
    }

    public void setCycle(boolean cycle) {
        this.cycle = cycle;
    }
    public String getIncrement() {
        return increment;
    }

    public void setIncrement(String increment) {
        this.increment = increment;
    }
    public String getMaxvalue() {
        return maxValue;
    }

    public void setMaxvalue(String maxValue) {
        this.maxValue = maxValue;
    }
    public String getStart() {
        return start;
    }

    public void setStart(String start) {
        this.start = start;
    }

    public database_Column getDatabase_column() {
        return database_column;
    }

    public void setDatabase_column(database_Column database_column) {
        this.database_column = database_column;
    }
    public List<database_Column> getDatabase_columns() {
        return database_columns;
    }

    public void addDatabase_column(Database_column database_column) {
        this.database_columns.add(database_column);
    }
    public database_TableContainer getDatabase_tablecontainer() {
        return database_tablecontainer;
    }

    public void setDatabase_tablecontainer(database_TableContainer database_tablecontainer) {
        this.database_tablecontainer = database_tablecontainer;
    }

}