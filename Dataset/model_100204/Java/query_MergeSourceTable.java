





import java.util.List;
import java.util.ArrayList;

public class query_MergeSourceTable extends SQLQueryObject {






    private List<query_QueryMergeStatement> query_querymergestatements;




    private query_QueryMergeStatement query_querymergestatement;




    private query_QueryMergeStatement query_querymergestatement;


    public query_MergeSourceTable(
    ) {
        super(
        );
        this.query_querymergestatements = new ArrayList<>();
    }

    public query_MergeSourceTable(
        ArrayList<query_QueryMergeStatement> query_querymergestatements    ) {
        this.query_querymergestatements = query_querymergestatements;
    }


    public List<query_QueryMergeStatement> getQuery_querymergestatements() {
        return query_querymergestatements;
    }

    public void addQuery_querymergestatement(Query_querymergestatement query_querymergestatement) {
        this.query_querymergestatements.add(query_querymergestatement);
    }
    public query_QueryMergeStatement getQuery_querymergestatement() {
        return query_querymergestatement;
    }

    public void setQuery_querymergestatement(query_QueryMergeStatement query_querymergestatement) {
        this.query_querymergestatement = query_querymergestatement;
    }
    public query_QueryMergeStatement getQuery_querymergestatement() {
        return query_querymergestatement;
    }

    public void setQuery_querymergestatement(query_QueryMergeStatement query_querymergestatement) {
        this.query_querymergestatement = query_querymergestatement;
    }

}