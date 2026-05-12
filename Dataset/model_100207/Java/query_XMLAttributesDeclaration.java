





import java.util.List;
import java.util.ArrayList;

public class query_XMLAttributesDeclaration  {






    private query_XMLValueFunctionElement query_xmlvaluefunctionelement;




    private query_XMLAttributeDeclarationItem query_xmlattributedeclarationitem;




    private List<query_XMLAttributeDeclarationItem> query_xmlattributedeclarationitems;




    private query_XMLValueFunctionElement query_xmlvaluefunctionelement;


    public query_XMLAttributesDeclaration(
    ) {
        this.query_xmlattributedeclarationitems = new ArrayList<>();
    }

    public query_XMLAttributesDeclaration(
        ArrayList<query_XMLAttributeDeclarationItem> query_xmlattributedeclarationitems    ) {
        this.query_xmlattributedeclarationitems = query_xmlattributedeclarationitems;
    }


    public query_XMLValueFunctionElement getQuery_xmlvaluefunctionelement() {
        return query_xmlvaluefunctionelement;
    }

    public void setQuery_xmlvaluefunctionelement(query_XMLValueFunctionElement query_xmlvaluefunctionelement) {
        this.query_xmlvaluefunctionelement = query_xmlvaluefunctionelement;
    }
    public query_XMLAttributeDeclarationItem getQuery_xmlattributedeclarationitem() {
        return query_xmlattributedeclarationitem;
    }

    public void setQuery_xmlattributedeclarationitem(query_XMLAttributeDeclarationItem query_xmlattributedeclarationitem) {
        this.query_xmlattributedeclarationitem = query_xmlattributedeclarationitem;
    }
    public List<query_XMLAttributeDeclarationItem> getQuery_xmlattributedeclarationitems() {
        return query_xmlattributedeclarationitems;
    }

    public void addQuery_xmlattributedeclarationitem(Query_xmlattributedeclarationitem query_xmlattributedeclarationitem) {
        this.query_xmlattributedeclarationitems.add(query_xmlattributedeclarationitem);
    }
    public query_XMLValueFunctionElement getQuery_xmlvaluefunctionelement() {
        return query_xmlvaluefunctionelement;
    }

    public void setQuery_xmlvaluefunctionelement(query_XMLValueFunctionElement query_xmlvaluefunctionelement) {
        this.query_xmlvaluefunctionelement = query_xmlvaluefunctionelement;
    }

}