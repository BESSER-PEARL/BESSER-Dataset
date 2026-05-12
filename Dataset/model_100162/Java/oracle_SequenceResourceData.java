





import java.util.List;
import java.util.ArrayList;

public class oracle_SequenceResourceData extends DatabaseResourceData {

    private boolean isHistory;
    private String increment;
    private String minValue;
    private String start;
    private boolean cycle;
    private String tableName;
    private String cache;
    private boolean useCache;
    private String maxValue;



    public oracle_SequenceResourceData(
        boolean isHistory,        String increment,        String minValue,        String start,        boolean cycle,        String tableName,        String cache,        boolean useCache,        String maxValue    ) {
        super(
        );
        this.isHistory = isHistory;
        this.increment = increment;
        this.minValue = minValue;
        this.start = start;
        this.cycle = cycle;
        this.tableName = tableName;
        this.cache = cache;
        this.useCache = useCache;
        this.maxValue = maxValue;
    }


    public boolean getIshistory() {
        return isHistory;
    }

    public void setIshistory(boolean isHistory) {
        this.isHistory = isHistory;
    }
    public String getIncrement() {
        return increment;
    }

    public void setIncrement(String increment) {
        this.increment = increment;
    }
    public String getMinvalue() {
        return minValue;
    }

    public void setMinvalue(String minValue) {
        this.minValue = minValue;
    }
    public String getStart() {
        return start;
    }

    public void setStart(String start) {
        this.start = start;
    }
    public boolean getCycle() {
        return cycle;
    }

    public void setCycle(boolean cycle) {
        this.cycle = cycle;
    }
    public String getTablename() {
        return tableName;
    }

    public void setTablename(String tableName) {
        this.tableName = tableName;
    }
    public String getCache() {
        return cache;
    }

    public void setCache(String cache) {
        this.cache = cache;
    }
    public boolean getUsecache() {
        return useCache;
    }

    public void setUsecache(boolean useCache) {
        this.useCache = useCache;
    }
    public String getMaxvalue() {
        return maxValue;
    }

    public void setMaxvalue(String maxValue) {
        this.maxValue = maxValue;
    }


}