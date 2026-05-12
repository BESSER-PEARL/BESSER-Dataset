





import java.util.List;
import java.util.ArrayList;

public class db_SafiResultSet extends DBResource {

    private String holdabilityMode;
    private String scrollMode;
    private boolean readOnly;
    private boolean scrollable;
    private boolean useCache;





    private db_Query db_query;




    private db_Query db_query;


    public db_SafiResultSet(
        String holdabilityMode,        String scrollMode,        boolean readOnly,        boolean scrollable,        boolean useCache    ) {
        super(
        );
        this.holdabilityMode = holdabilityMode;
        this.scrollMode = scrollMode;
        this.readOnly = readOnly;
        this.scrollable = scrollable;
        this.useCache = useCache;
    }


    public String getHoldabilitymode() {
        return holdabilityMode;
    }

    public void setHoldabilitymode(String holdabilityMode) {
        this.holdabilityMode = holdabilityMode;
    }
    public String getScrollmode() {
        return scrollMode;
    }

    public void setScrollmode(String scrollMode) {
        this.scrollMode = scrollMode;
    }
    public boolean getReadonly() {
        return readOnly;
    }

    public void setReadonly(boolean readOnly) {
        this.readOnly = readOnly;
    }
    public boolean getScrollable() {
        return scrollable;
    }

    public void setScrollable(boolean scrollable) {
        this.scrollable = scrollable;
    }
    public boolean getUsecache() {
        return useCache;
    }

    public void setUsecache(boolean useCache) {
        this.useCache = useCache;
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