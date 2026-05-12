





import java.util.List;
import java.util.ArrayList;

public class query_XMLNamespacesDeclaration extends SQLQueryObject {






    private query_XMLValueFunctionElement query_xmlvaluefunctionelement;




    private query_XMLNamespaceDeclarationItem query_xmlnamespacedeclarationitem;




    private query_XMLValueFunctionElement query_xmlvaluefunctionelement;




    private query_XMLValueFunctionForest query_xmlvaluefunctionforest;




    private List<query_XMLNamespaceDeclarationItem> query_xmlnamespacedeclarationitems;




    private query_XMLValueFunctionForest query_xmlvaluefunctionforest;


    public query_XMLNamespacesDeclaration(
    ) {
        super(
        );
        this.query_xmlnamespacedeclarationitems = new ArrayList<>();
    }

    public query_XMLNamespacesDeclaration(
        ArrayList<query_XMLNamespaceDeclarationItem> query_xmlnamespacedeclarationitems    ) {
        this.query_xmlnamespacedeclarationitems = query_xmlnamespacedeclarationitems;
    }


    public query_XMLValueFunctionElement getQuery_xmlvaluefunctionelement() {
        return query_xmlvaluefunctionelement;
    }

    public void setQuery_xmlvaluefunctionelement(query_XMLValueFunctionElement query_xmlvaluefunctionelement) {
        this.query_xmlvaluefunctionelement = query_xmlvaluefunctionelement;
    }
    public query_XMLNamespaceDeclarationItem getQuery_xmlnamespacedeclarationitem() {
        return query_xmlnamespacedeclarationitem;
    }

    public void setQuery_xmlnamespacedeclarationitem(query_XMLNamespaceDeclarationItem query_xmlnamespacedeclarationitem) {
        this.query_xmlnamespacedeclarationitem = query_xmlnamespacedeclarationitem;
    }
    public query_XMLValueFunctionElement getQuery_xmlvaluefunctionelement() {
        return query_xmlvaluefunctionelement;
    }

    public void setQuery_xmlvaluefunctionelement(query_XMLValueFunctionElement query_xmlvaluefunctionelement) {
        this.query_xmlvaluefunctionelement = query_xmlvaluefunctionelement;
    }
    public query_XMLValueFunctionForest getQuery_xmlvaluefunctionforest() {
        return query_xmlvaluefunctionforest;
    }

    public void setQuery_xmlvaluefunctionforest(query_XMLValueFunctionForest query_xmlvaluefunctionforest) {
        this.query_xmlvaluefunctionforest = query_xmlvaluefunctionforest;
    }
    public List<query_XMLNamespaceDeclarationItem> getQuery_xmlnamespacedeclarationitems() {
        return query_xmlnamespacedeclarationitems;
    }

    public void addQuery_xmlnamespacedeclarationitem(Query_xmlnamespacedeclarationitem query_xmlnamespacedeclarationitem) {
        this.query_xmlnamespacedeclarationitems.add(query_xmlnamespacedeclarationitem);
    }
    public query_XMLValueFunctionForest getQuery_xmlvaluefunctionforest() {
        return query_xmlvaluefunctionforest;
    }

    public void setQuery_xmlvaluefunctionforest(query_XMLValueFunctionForest query_xmlvaluefunctionforest) {
        this.query_xmlvaluefunctionforest = query_xmlvaluefunctionforest;
    }

}