





import java.util.List;
import java.util.ArrayList;

public class jDOQL_ImportClause  {

    private String importDeclarations;





    private jDOQL_SingleStringJDOQL jdoql_singlestringjdoql;


    public jDOQL_ImportClause(
        String importDeclarations    ) {
        this.importDeclarations = importDeclarations;
    }


    public String getImportdeclarations() {
        return importDeclarations;
    }

    public void setImportdeclarations(String importDeclarations) {
        this.importDeclarations = importDeclarations;
    }

    public jDOQL_SingleStringJDOQL getJdoql_singlestringjdoql() {
        return jdoql_singlestringjdoql;
    }

    public void setJdoql_singlestringjdoql(jDOQL_SingleStringJDOQL jdoql_singlestringjdoql) {
        this.jdoql_singlestringjdoql = jdoql_singlestringjdoql;
    }

}