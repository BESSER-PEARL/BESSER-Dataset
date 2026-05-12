





import java.util.List;
import java.util.ArrayList;

public class query_QuerySelect extends QueryExpressionBody {

    private boolean distinct;





    private query_QueryResultSpecification query_queryresultspecification;




    private query_QuerySearchCondition query_querysearchcondition;




    private query_TableReference query_tablereference;




    private query_QuerySearchCondition query_querysearchcondition;




    private List<query_GroupingSpecification> query_groupingspecifications;




    private query_QuerySearchCondition query_querysearchcondition;




    private query_QuerySearchCondition query_querysearchcondition;




    private List<query_TableReference> query_tablereferences;




    private List<query_QueryResultSpecification> query_queryresultspecifications;




    private query_GroupingSpecification query_groupingspecification;


    public query_QuerySelect(
        boolean distinct    ) {
        super(
        );
        this.distinct = distinct;
        this.query_groupingspecifications = new ArrayList<>();
        this.query_tablereferences = new ArrayList<>();
        this.query_queryresultspecifications = new ArrayList<>();
    }

    public query_QuerySelect(
        boolean distinct        ArrayList<query_GroupingSpecification> query_groupingspecifications,        ArrayList<query_TableReference> query_tablereferences,        ArrayList<query_QueryResultSpecification> query_queryresultspecifications    ) {
        this.distinct = distinct;
        this.query_groupingspecifications = query_groupingspecifications;
        this.query_tablereferences = query_tablereferences;
        this.query_queryresultspecifications = query_queryresultspecifications;
    }

    public boolean getDistinct() {
        return distinct;
    }

    public void setDistinct(boolean distinct) {
        this.distinct = distinct;
    }

    public query_QueryResultSpecification getQuery_queryresultspecification() {
        return query_queryresultspecification;
    }

    public void setQuery_queryresultspecification(query_QueryResultSpecification query_queryresultspecification) {
        this.query_queryresultspecification = query_queryresultspecification;
    }
    public query_QuerySearchCondition getQuery_querysearchcondition() {
        return query_querysearchcondition;
    }

    public void setQuery_querysearchcondition(query_QuerySearchCondition query_querysearchcondition) {
        this.query_querysearchcondition = query_querysearchcondition;
    }
    public query_TableReference getQuery_tablereference() {
        return query_tablereference;
    }

    public void setQuery_tablereference(query_TableReference query_tablereference) {
        this.query_tablereference = query_tablereference;
    }
    public query_QuerySearchCondition getQuery_querysearchcondition() {
        return query_querysearchcondition;
    }

    public void setQuery_querysearchcondition(query_QuerySearchCondition query_querysearchcondition) {
        this.query_querysearchcondition = query_querysearchcondition;
    }
    public List<query_GroupingSpecification> getQuery_groupingspecifications() {
        return query_groupingspecifications;
    }

    public void addQuery_groupingspecification(Query_groupingspecification query_groupingspecification) {
        this.query_groupingspecifications.add(query_groupingspecification);
    }
    public query_QuerySearchCondition getQuery_querysearchcondition() {
        return query_querysearchcondition;
    }

    public void setQuery_querysearchcondition(query_QuerySearchCondition query_querysearchcondition) {
        this.query_querysearchcondition = query_querysearchcondition;
    }
    public query_QuerySearchCondition getQuery_querysearchcondition() {
        return query_querysearchcondition;
    }

    public void setQuery_querysearchcondition(query_QuerySearchCondition query_querysearchcondition) {
        this.query_querysearchcondition = query_querysearchcondition;
    }
    public List<query_TableReference> getQuery_tablereferences() {
        return query_tablereferences;
    }

    public void addQuery_tablereference(Query_tablereference query_tablereference) {
        this.query_tablereferences.add(query_tablereference);
    }
    public List<query_QueryResultSpecification> getQuery_queryresultspecifications() {
        return query_queryresultspecifications;
    }

    public void addQuery_queryresultspecification(Query_queryresultspecification query_queryresultspecification) {
        this.query_queryresultspecifications.add(query_queryresultspecification);
    }
    public query_GroupingSpecification getQuery_groupingspecification() {
        return query_groupingspecification;
    }

    public void setQuery_groupingspecification(query_GroupingSpecification query_groupingspecification) {
        this.query_groupingspecification = query_groupingspecification;
    }

}