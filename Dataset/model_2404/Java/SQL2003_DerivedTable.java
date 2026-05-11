





import java.util.List;
import java.util.ArrayList;

public class SQL2003_DerivedTable extends Table {

    private String query_expression;



    public SQL2003_DerivedTable(
        String query_expression    ) {
        super(
        );
        this.query_expression = query_expression;
    }


    public String getQuery_expression() {
        return query_expression;
    }

    public void setQuery_expression(String query_expression) {
        this.query_expression = query_expression;
    }


}