





import java.util.List;
import java.util.ArrayList;

public class jDOQL_SelectClause extends SubquerySelectClause {

    private boolean isUnique;





    private jDOQL_SingleStringJDOQL jdoql_singlestringjdoql;


    public jDOQL_SelectClause(
        boolean isUnique    ) {
        super(
        );
        this.isUnique = isUnique;
    }


    public boolean getIsunique() {
        return isUnique;
    }

    public void setIsunique(boolean isUnique) {
        this.isUnique = isUnique;
    }

    public jDOQL_SingleStringJDOQL getJdoql_singlestringjdoql() {
        return jdoql_singlestringjdoql;
    }

    public void setJdoql_singlestringjdoql(jDOQL_SingleStringJDOQL jdoql_singlestringjdoql) {
        this.jdoql_singlestringjdoql = jdoql_singlestringjdoql;
    }

}