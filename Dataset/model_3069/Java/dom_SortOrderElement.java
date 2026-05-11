





import java.util.List;
import java.util.ArrayList;

public class dom_SortOrderElement  {

    private String sortOrder;





    private dom_Expression dom_expression;




    private dom_SelectStatement dom_selectstatement;


    public dom_SortOrderElement(
        String sortOrder    ) {
        this.sortOrder = sortOrder;
    }


    public String getSortorder() {
        return sortOrder;
    }

    public void setSortorder(String sortOrder) {
        this.sortOrder = sortOrder;
    }

    public dom_Expression getDom_expression() {
        return dom_expression;
    }

    public void setDom_expression(dom_Expression dom_expression) {
        this.dom_expression = dom_expression;
    }
    public dom_SelectStatement getDom_selectstatement() {
        return dom_selectstatement;
    }

    public void setDom_selectstatement(dom_SelectStatement dom_selectstatement) {
        this.dom_selectstatement = dom_selectstatement;
    }

}