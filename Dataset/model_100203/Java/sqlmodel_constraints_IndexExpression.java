





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_constraints_IndexExpression extends SQLObject {

    private String sql;



    public sqlmodel_constraints_IndexExpression(
        String sql    ) {
        super(
        );
        this.sql = sql;
    }


    public String getSql() {
        return sql;
    }

    public void setSql(String sql) {
        this.sql = sql;
    }


}