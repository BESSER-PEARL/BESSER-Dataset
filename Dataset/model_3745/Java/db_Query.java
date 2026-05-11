





import java.util.List;
import java.util.ArrayList;

public class db_Query extends DBResource {

    private String catalog;
    private String queryType;
    private String querySql;



    public db_Query(
        String catalog,        String queryType,        String querySql    ) {
        super(
        );
        this.catalog = catalog;
        this.queryType = queryType;
        this.querySql = querySql;
    }


    public String getCatalog() {
        return catalog;
    }

    public void setCatalog(String catalog) {
        this.catalog = catalog;
    }
    public String getQuerytype() {
        return queryType;
    }

    public void setQuerytype(String queryType) {
        this.queryType = queryType;
    }
    public String getQuerysql() {
        return querySql;
    }

    public void setQuerysql(String querySql) {
        this.querySql = querySql;
    }


}