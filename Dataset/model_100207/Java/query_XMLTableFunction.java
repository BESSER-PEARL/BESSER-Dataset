





import java.util.List;
import java.util.ArrayList;

public class query_XMLTableFunction extends TableFunction {

    private String tableRowPattern;





    private query_XMLQueryArgumentList query_xmlqueryargumentlist;




    private query_XMLNamespacesDeclaration query_xmlnamespacesdeclaration;




    private query_XMLTableColumnDefinitionItem query_xmltablecolumndefinitionitem;




    private query_XMLQueryArgumentList query_xmlqueryargumentlist;




    private List<query_XMLTableColumnDefinitionItem> query_xmltablecolumndefinitionitems;




    private query_XMLNamespacesDeclaration query_xmlnamespacesdeclaration;


    public query_XMLTableFunction(
        String tableRowPattern    ) {
        super(
        );
        this.tableRowPattern = tableRowPattern;
        this.query_xmltablecolumndefinitionitems = new ArrayList<>();
    }

    public query_XMLTableFunction(
        String tableRowPattern        ArrayList<query_XMLTableColumnDefinitionItem> query_xmltablecolumndefinitionitems    ) {
        this.tableRowPattern = tableRowPattern;
        this.query_xmltablecolumndefinitionitems = query_xmltablecolumndefinitionitems;
    }

    public String getTablerowpattern() {
        return tableRowPattern;
    }

    public void setTablerowpattern(String tableRowPattern) {
        this.tableRowPattern = tableRowPattern;
    }

    public query_XMLQueryArgumentList getQuery_xmlqueryargumentlist() {
        return query_xmlqueryargumentlist;
    }

    public void setQuery_xmlqueryargumentlist(query_XMLQueryArgumentList query_xmlqueryargumentlist) {
        this.query_xmlqueryargumentlist = query_xmlqueryargumentlist;
    }
    public query_XMLNamespacesDeclaration getQuery_xmlnamespacesdeclaration() {
        return query_xmlnamespacesdeclaration;
    }

    public void setQuery_xmlnamespacesdeclaration(query_XMLNamespacesDeclaration query_xmlnamespacesdeclaration) {
        this.query_xmlnamespacesdeclaration = query_xmlnamespacesdeclaration;
    }
    public query_XMLTableColumnDefinitionItem getQuery_xmltablecolumndefinitionitem() {
        return query_xmltablecolumndefinitionitem;
    }

    public void setQuery_xmltablecolumndefinitionitem(query_XMLTableColumnDefinitionItem query_xmltablecolumndefinitionitem) {
        this.query_xmltablecolumndefinitionitem = query_xmltablecolumndefinitionitem;
    }
    public query_XMLQueryArgumentList getQuery_xmlqueryargumentlist() {
        return query_xmlqueryargumentlist;
    }

    public void setQuery_xmlqueryargumentlist(query_XMLQueryArgumentList query_xmlqueryargumentlist) {
        this.query_xmlqueryargumentlist = query_xmlqueryargumentlist;
    }
    public List<query_XMLTableColumnDefinitionItem> getQuery_xmltablecolumndefinitionitems() {
        return query_xmltablecolumndefinitionitems;
    }

    public void addQuery_xmltablecolumndefinitionitem(Query_xmltablecolumndefinitionitem query_xmltablecolumndefinitionitem) {
        this.query_xmltablecolumndefinitionitems.add(query_xmltablecolumndefinitionitem);
    }
    public query_XMLNamespacesDeclaration getQuery_xmlnamespacesdeclaration() {
        return query_xmlnamespacesdeclaration;
    }

    public void setQuery_xmlnamespacesdeclaration(query_XMLNamespacesDeclaration query_xmlnamespacesdeclaration) {
        this.query_xmlnamespacesdeclaration = query_xmlnamespacesdeclaration;
    }

}