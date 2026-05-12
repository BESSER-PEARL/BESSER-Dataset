





import java.util.List;
import java.util.ArrayList;

public class query_XMLQueryArgumentList extends SQLQueryObject {

    private String passingMechanism;





    private List<query_XMLQueryArgumentItem> query_xmlqueryargumentitems;




    private query_XMLValueFunctionQuery query_xmlvaluefunctionquery;




    private query_XMLValueFunctionQuery query_xmlvaluefunctionquery;




    private query_XMLQueryArgumentItem query_xmlqueryargumentitem;


    public query_XMLQueryArgumentList(
        String passingMechanism    ) {
        super(
        );
        this.passingMechanism = passingMechanism;
        this.query_xmlqueryargumentitems = new ArrayList<>();
    }

    public query_XMLQueryArgumentList(
        String passingMechanism        ArrayList<query_XMLQueryArgumentItem> query_xmlqueryargumentitems    ) {
        this.passingMechanism = passingMechanism;
        this.query_xmlqueryargumentitems = query_xmlqueryargumentitems;
    }

    public String getPassingmechanism() {
        return passingMechanism;
    }

    public void setPassingmechanism(String passingMechanism) {
        this.passingMechanism = passingMechanism;
    }

    public List<query_XMLQueryArgumentItem> getQuery_xmlqueryargumentitems() {
        return query_xmlqueryargumentitems;
    }

    public void addQuery_xmlqueryargumentitem(Query_xmlqueryargumentitem query_xmlqueryargumentitem) {
        this.query_xmlqueryargumentitems.add(query_xmlqueryargumentitem);
    }
    public query_XMLValueFunctionQuery getQuery_xmlvaluefunctionquery() {
        return query_xmlvaluefunctionquery;
    }

    public void setQuery_xmlvaluefunctionquery(query_XMLValueFunctionQuery query_xmlvaluefunctionquery) {
        this.query_xmlvaluefunctionquery = query_xmlvaluefunctionquery;
    }
    public query_XMLValueFunctionQuery getQuery_xmlvaluefunctionquery() {
        return query_xmlvaluefunctionquery;
    }

    public void setQuery_xmlvaluefunctionquery(query_XMLValueFunctionQuery query_xmlvaluefunctionquery) {
        this.query_xmlvaluefunctionquery = query_xmlvaluefunctionquery;
    }
    public query_XMLQueryArgumentItem getQuery_xmlqueryargumentitem() {
        return query_xmlqueryargumentitem;
    }

    public void setQuery_xmlqueryargumentitem(query_XMLQueryArgumentItem query_xmlqueryargumentitem) {
        this.query_xmlqueryargumentitem = query_xmlqueryargumentitem;
    }

}