





import java.util.List;
import java.util.ArrayList;

public class query_ValueExpressionCaseSearch extends ValueExpressionCase {






    private query_ValueExpressionCaseSearchContent query_valueexpressioncasesearchcontent;




    private List<query_ValueExpressionCaseSearchContent> query_valueexpressioncasesearchcontents;


    public query_ValueExpressionCaseSearch(
    ) {
        super(
        );
        this.query_valueexpressioncasesearchcontents = new ArrayList<>();
    }

    public query_ValueExpressionCaseSearch(
        ArrayList<query_ValueExpressionCaseSearchContent> query_valueexpressioncasesearchcontents    ) {
        this.query_valueexpressioncasesearchcontents = query_valueexpressioncasesearchcontents;
    }


    public query_ValueExpressionCaseSearchContent getQuery_valueexpressioncasesearchcontent() {
        return query_valueexpressioncasesearchcontent;
    }

    public void setQuery_valueexpressioncasesearchcontent(query_ValueExpressionCaseSearchContent query_valueexpressioncasesearchcontent) {
        this.query_valueexpressioncasesearchcontent = query_valueexpressioncasesearchcontent;
    }
    public List<query_ValueExpressionCaseSearchContent> getQuery_valueexpressioncasesearchcontents() {
        return query_valueexpressioncasesearchcontents;
    }

    public void addQuery_valueexpressioncasesearchcontent(Query_valueexpressioncasesearchcontent query_valueexpressioncasesearchcontent) {
        this.query_valueexpressioncasesearchcontents.add(query_valueexpressioncasesearchcontent);
    }

}