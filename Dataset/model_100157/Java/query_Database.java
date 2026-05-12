





import java.util.List;
import java.util.ArrayList;

public class query_Database  {

    private String url;
    private String name;
    private String port;
    private String dbName;





    private query_Model query_model;


    public query_Database(
        String url,        String name,        String port,        String dbName    ) {
        this.url = url;
        this.name = name;
        this.port = port;
        this.dbName = dbName;
    }


    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPort() {
        return port;
    }

    public void setPort(String port) {
        this.port = port;
    }
    public String getDbname() {
        return dbName;
    }

    public void setDbname(String dbName) {
        this.dbName = dbName;
    }

    public query_Model getQuery_model() {
        return query_model;
    }

    public void setQuery_model(query_Model query_model) {
        this.query_model = query_model;
    }

}