





import java.util.List;
import java.util.ArrayList;

public class jDOQL_FromClause  {

    private boolean isExcludeSubclasses;
    private String candidateClassName;





    private jDOQL_SingleStringJDOQL jdoql_singlestringjdoql;


    public jDOQL_FromClause(
        boolean isExcludeSubclasses,        String candidateClassName    ) {
        this.isExcludeSubclasses = isExcludeSubclasses;
        this.candidateClassName = candidateClassName;
    }


    public boolean getIsexcludesubclasses() {
        return isExcludeSubclasses;
    }

    public void setIsexcludesubclasses(boolean isExcludeSubclasses) {
        this.isExcludeSubclasses = isExcludeSubclasses;
    }
    public String getCandidateclassname() {
        return candidateClassName;
    }

    public void setCandidateclassname(String candidateClassName) {
        this.candidateClassName = candidateClassName;
    }

    public jDOQL_SingleStringJDOQL getJdoql_singlestringjdoql() {
        return jdoql_singlestringjdoql;
    }

    public void setJdoql_singlestringjdoql(jDOQL_SingleStringJDOQL jdoql_singlestringjdoql) {
        this.jdoql_singlestringjdoql = jdoql_singlestringjdoql;
    }

}