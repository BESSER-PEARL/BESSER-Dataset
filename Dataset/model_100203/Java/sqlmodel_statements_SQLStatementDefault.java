





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_statements_SQLStatementDefault extends statements_SQLStatement, schema_SQLObject {

    private String SQL;



    public sqlmodel_statements_SQLStatementDefault(
        String SQL    ) {
        super(
        );
        this.SQL = SQL;
    }


    public String getSql() {
        return SQL;
    }

    public void setSql(String SQL) {
        this.SQL = SQL;
    }


}