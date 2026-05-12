





import java.util.List;
import java.util.ArrayList;

public class db_Query extends DBResource {

    private String queryType;
    private String catalog;
    private String querySql;



    public db_Query(
        String queryType,        String catalog,        String querySql    ) {
        super(
        );
        this.queryType = queryType;
        this.catalog = catalog;
        this.querySql = querySql;
    }


    public String getQuerytype() {
        return queryType;
    }

    public void setQuerytype(String queryType) {
        this.queryType = queryType;
    }
    public String getCatalog() {
        return catalog;
    }

    public void setCatalog(String catalog) {
        this.catalog = catalog;
    }
    public String getQuerysql() {
        return querySql;
    }

    public void setQuerysql(String querySql) {
        this.querySql = querySql;
    }


}