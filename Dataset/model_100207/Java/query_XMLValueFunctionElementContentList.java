





import java.util.List;
import java.util.ArrayList;

public class query_XMLValueFunctionElementContentList extends SQLQueryObject {

    private String nullHandlingOption;





    private query_XMLValueFunctionElement query_xmlvaluefunctionelement;




    private query_XMLValueFunctionElementContentItem query_xmlvaluefunctionelementcontentitem;




    private query_XMLValueFunctionElement query_xmlvaluefunctionelement;




    private List<query_XMLValueFunctionElementContentItem> query_xmlvaluefunctionelementcontentitems;


    public query_XMLValueFunctionElementContentList(
        String nullHandlingOption    ) {
        super(
        );
        this.nullHandlingOption = nullHandlingOption;
        this.query_xmlvaluefunctionelementcontentitems = new ArrayList<>();
    }

    public query_XMLValueFunctionElementContentList(
        String nullHandlingOption        ArrayList<query_XMLValueFunctionElementContentItem> query_xmlvaluefunctionelementcontentitems    ) {
        this.nullHandlingOption = nullHandlingOption;
        this.query_xmlvaluefunctionelementcontentitems = query_xmlvaluefunctionelementcontentitems;
    }

    public String getNullhandlingoption() {
        return nullHandlingOption;
    }

    public void setNullhandlingoption(String nullHandlingOption) {
        this.nullHandlingOption = nullHandlingOption;
    }

    public query_XMLValueFunctionElement getQuery_xmlvaluefunctionelement() {
        return query_xmlvaluefunctionelement;
    }

    public void setQuery_xmlvaluefunctionelement(query_XMLValueFunctionElement query_xmlvaluefunctionelement) {
        this.query_xmlvaluefunctionelement = query_xmlvaluefunctionelement;
    }
    public query_XMLValueFunctionElementContentItem getQuery_xmlvaluefunctionelementcontentitem() {
        return query_xmlvaluefunctionelementcontentitem;
    }

    public void setQuery_xmlvaluefunctionelementcontentitem(query_XMLValueFunctionElementContentItem query_xmlvaluefunctionelementcontentitem) {
        this.query_xmlvaluefunctionelementcontentitem = query_xmlvaluefunctionelementcontentitem;
    }
    public query_XMLValueFunctionElement getQuery_xmlvaluefunctionelement() {
        return query_xmlvaluefunctionelement;
    }

    public void setQuery_xmlvaluefunctionelement(query_XMLValueFunctionElement query_xmlvaluefunctionelement) {
        this.query_xmlvaluefunctionelement = query_xmlvaluefunctionelement;
    }
    public List<query_XMLValueFunctionElementContentItem> getQuery_xmlvaluefunctionelementcontentitems() {
        return query_xmlvaluefunctionelementcontentitems;
    }

    public void addQuery_xmlvaluefunctionelementcontentitem(Query_xmlvaluefunctionelementcontentitem query_xmlvaluefunctionelementcontentitem) {
        this.query_xmlvaluefunctionelementcontentitems.add(query_xmlvaluefunctionelementcontentitem);
    }

}