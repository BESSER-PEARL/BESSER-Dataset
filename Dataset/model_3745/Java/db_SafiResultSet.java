





import java.util.List;
import java.util.ArrayList;

public class db_SafiResultSet extends DBResource {

    private boolean readOnly;
    private boolean useCache;
    private String scrollMode;
    private boolean scrollable;
    private String holdabilityMode;





    private db_Query db_query;




    private db_Query db_query;


    public db_SafiResultSet(
        boolean readOnly,        boolean useCache,        String scrollMode,        boolean scrollable,        String holdabilityMode    ) {
        super(
        );
        this.readOnly = readOnly;
        this.useCache = useCache;
        this.scrollMode = scrollMode;
        this.scrollable = scrollable;
        this.holdabilityMode = holdabilityMode;
    }


    public boolean getReadonly() {
        return readOnly;
    }

    public void setReadonly(boolean readOnly) {
        this.readOnly = readOnly;
    }
    public boolean getUsecache() {
        return useCache;
    }

    public void setUsecache(boolean useCache) {
        this.useCache = useCache;
    }
    public String getScrollmode() {
        return scrollMode;
    }

    public void setScrollmode(String scrollMode) {
        this.scrollMode = scrollMode;
    }
    public boolean getScrollable() {
        return scrollable;
    }

    public void setScrollable(boolean scrollable) {
        this.scrollable = scrollable;
    }
    public String getHoldabilitymode() {
        return holdabilityMode;
    }

    public void setHoldabilitymode(String holdabilityMode) {
        this.holdabilityMode = holdabilityMode;
    }

    public db_Query getDb_query() {
        return db_query;
    }

    public void setDb_query(db_Query db_query) {
        this.db_query = db_query;
    }
    public db_Query getDb_query() {
        return db_query;
    }

    public void setDb_query(db_Query db_query) {
        this.db_query = db_query;
    }

}