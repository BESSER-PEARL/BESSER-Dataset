





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_expressions_SearchConditionDefault extends expressions_SearchCondition, schema_SQLObject {

    private String SQL;



    public sqlmodel_expressions_SearchConditionDefault(
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