





import java.util.List;
import java.util.ArrayList;

public class database_Sequence extends NamedElement {

    private String minValue;
    private String cacheSize;
    private boolean cycle;
    private String start;
    private String maxValue;
    private String increment;





    private database_TableContainer database_tablecontainer;


    public database_Sequence(
        String minValue,        String cacheSize,        boolean cycle,        String start,        String maxValue,        String increment    ) {
        super(
        );
        this.minValue = minValue;
        this.cacheSize = cacheSize;
        this.cycle = cycle;
        this.start = start;
        this.maxValue = maxValue;
        this.increment = increment;
    }


    public String getMinvalue() {
        return minValue;
    }

    public void setMinvalue(String minValue) {
        this.minValue = minValue;
    }
    public String getCachesize() {
        return cacheSize;
    }

    public void setCachesize(String cacheSize) {
        this.cacheSize = cacheSize;
    }
    public boolean getCycle() {
        return cycle;
    }

    public void setCycle(boolean cycle) {
        this.cycle = cycle;
    }
    public String getStart() {
        return start;
    }

    public void setStart(String start) {
        this.start = start;
    }
    public String getMaxvalue() {
        return maxValue;
    }

    public void setMaxvalue(String maxValue) {
        this.maxValue = maxValue;
    }
    public String getIncrement() {
        return increment;
    }

    public void setIncrement(String increment) {
        this.increment = increment;
    }

    public database_TableContainer getDatabase_tablecontainer() {
        return database_tablecontainer;
    }

    public void setDatabase_tablecontainer(database_TableContainer database_tablecontainer) {
        this.database_tablecontainer = database_tablecontainer;
    }

}