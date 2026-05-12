





import java.util.List;
import java.util.ArrayList;

public class db_DBConnection extends DBResource {

    private String password;
    private String user;
    private int maxPoolSize;
    private String url;
    private int loginTimeout;
    private String properties;
    private int maxIdleTime;
    private int minPoolSize;
    private int acquireIncrement;
    private String transactionMode;





    private db_DBDriver db_dbdriver;




    private db_DBDriver db_dbdriver;




    private db_Query db_query;




    private List<db_Query> db_querys;


    public db_DBConnection(
        String password,        String user,        int maxPoolSize,        String url,        int loginTimeout,        String properties,        int maxIdleTime,        int minPoolSize,        int acquireIncrement,        String transactionMode    ) {
        super(
        );
        this.password = password;
        this.user = user;
        this.maxPoolSize = maxPoolSize;
        this.url = url;
        this.loginTimeout = loginTimeout;
        this.properties = properties;
        this.maxIdleTime = maxIdleTime;
        this.minPoolSize = minPoolSize;
        this.acquireIncrement = acquireIncrement;
        this.transactionMode = transactionMode;
        this.db_querys = new ArrayList<>();
    }

    public db_DBConnection(
        String password,        String user,        int maxPoolSize,        String url,        int loginTimeout,        String properties,        int maxIdleTime,        int minPoolSize,        int acquireIncrement,        String transactionMode        ArrayList<db_Query> db_querys    ) {
        this.password = password;
        this.user = user;
        this.maxPoolSize = maxPoolSize;
        this.url = url;
        this.loginTimeout = loginTimeout;
        this.properties = properties;
        this.maxIdleTime = maxIdleTime;
        this.minPoolSize = minPoolSize;
        this.acquireIncrement = acquireIncrement;
        this.transactionMode = transactionMode;
        this.db_querys = db_querys;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getUser() {
        return user;
    }

    public void setUser(String user) {
        this.user = user;
    }
    public int getMaxpoolsize() {
        return maxPoolSize;
    }

    public void setMaxpoolsize(int maxPoolSize) {
        this.maxPoolSize = maxPoolSize;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public int getLogintimeout() {
        return loginTimeout;
    }

    public void setLogintimeout(int loginTimeout) {
        this.loginTimeout = loginTimeout;
    }
    public String getProperties() {
        return properties;
    }

    public void setProperties(String properties) {
        this.properties = properties;
    }
    public int getMaxidletime() {
        return maxIdleTime;
    }

    public void setMaxidletime(int maxIdleTime) {
        this.maxIdleTime = maxIdleTime;
    }
    public int getMinpoolsize() {
        return minPoolSize;
    }

    public void setMinpoolsize(int minPoolSize) {
        this.minPoolSize = minPoolSize;
    }
    public int getAcquireincrement() {
        return acquireIncrement;
    }

    public void setAcquireincrement(int acquireIncrement) {
        this.acquireIncrement = acquireIncrement;
    }
    public String getTransactionmode() {
        return transactionMode;
    }

    public void setTransactionmode(String transactionMode) {
        this.transactionMode = transactionMode;
    }

    public db_DBDriver getDb_dbdriver() {
        return db_dbdriver;
    }

    public void setDb_dbdriver(db_DBDriver db_dbdriver) {
        this.db_dbdriver = db_dbdriver;
    }
    public db_DBDriver getDb_dbdriver() {
        return db_dbdriver;
    }

    public void setDb_dbdriver(db_DBDriver db_dbdriver) {
        this.db_dbdriver = db_dbdriver;
    }
    public db_Query getDb_query() {
        return db_query;
    }

    public void setDb_query(db_Query db_query) {
        this.db_query = db_query;
    }
    public List<db_Query> getDb_querys() {
        return db_querys;
    }

    public void addDb_query(Db_query db_query) {
        this.db_querys.add(db_query);
    }

}