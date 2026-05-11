





import java.util.List;
import java.util.ArrayList;

public class dom_Join extends JoinEntity {

    private boolean fetch;
    private String type;
    private boolean propertyFetch;





    private dom_SelectStatement dom_selectstatement;




    private dom_Attribute dom_attribute;




    private dom_Expression dom_expression;


    public dom_Join(
        boolean fetch,        String type,        boolean propertyFetch    ) {
        super(
        );
        this.fetch = fetch;
        this.type = type;
        this.propertyFetch = propertyFetch;
    }


    public boolean getFetch() {
        return fetch;
    }

    public void setFetch(boolean fetch) {
        this.fetch = fetch;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getPropertyfetch() {
        return propertyFetch;
    }

    public void setPropertyfetch(boolean propertyFetch) {
        this.propertyFetch = propertyFetch;
    }

    public dom_SelectStatement getDom_selectstatement() {
        return dom_selectstatement;
    }

    public void setDom_selectstatement(dom_SelectStatement dom_selectstatement) {
        this.dom_selectstatement = dom_selectstatement;
    }
    public dom_Attribute getDom_attribute() {
        return dom_attribute;
    }

    public void setDom_attribute(dom_Attribute dom_attribute) {
        this.dom_attribute = dom_attribute;
    }
    public dom_Expression getDom_expression() {
        return dom_expression;
    }

    public void setDom_expression(dom_Expression dom_expression) {
        this.dom_expression = dom_expression;
    }

}