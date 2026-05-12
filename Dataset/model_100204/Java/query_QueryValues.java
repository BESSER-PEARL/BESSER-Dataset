





import java.util.List;
import java.util.ArrayList;

public class query_QueryValues extends QueryExpressionBody {






    private List<query_ValuesRow> query_valuesrows;




    private query_ValuesRow query_valuesrow;


    public query_QueryValues(
    ) {
        super(
        );
        this.query_valuesrows = new ArrayList<>();
    }

    public query_QueryValues(
        ArrayList<query_ValuesRow> query_valuesrows    ) {
        this.query_valuesrows = query_valuesrows;
    }


    public List<query_ValuesRow> getQuery_valuesrows() {
        return query_valuesrows;
    }

    public void addQuery_valuesrow(Query_valuesrow query_valuesrow) {
        this.query_valuesrows.add(query_valuesrow);
    }
    public query_ValuesRow getQuery_valuesrow() {
        return query_valuesrow;
    }

    public void setQuery_valuesrow(query_ValuesRow query_valuesrow) {
        this.query_valuesrow = query_valuesrow;
    }

}