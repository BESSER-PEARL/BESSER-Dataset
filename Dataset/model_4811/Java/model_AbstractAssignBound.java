





import java.util.List;
import java.util.ArrayList;

public class model_AbstractAssignBound  {






    private model_Variable model_variable;




    private Property property;




    private Part part;




    private model_PartnerLink model_partnerlink;




    private model_Query model_query;




    private model_Expression model_expression;


    public model_AbstractAssignBound(
    ) {
    }



    public model_Variable getModel_variable() {
        return model_variable;
    }

    public void setModel_variable(model_Variable model_variable) {
        this.model_variable = model_variable;
    }
    public Property getProperty() {
        return property;
    }

    public void setProperty(Property property) {
        this.property = property;
    }
    public Part getPart() {
        return part;
    }

    public void setPart(Part part) {
        this.part = part;
    }
    public model_PartnerLink getModel_partnerlink() {
        return model_partnerlink;
    }

    public void setModel_partnerlink(model_PartnerLink model_partnerlink) {
        this.model_partnerlink = model_partnerlink;
    }
    public model_Query getModel_query() {
        return model_query;
    }

    public void setModel_query(model_Query model_query) {
        this.model_query = model_query;
    }
    public model_Expression getModel_expression() {
        return model_expression;
    }

    public void setModel_expression(model_Expression model_expression) {
        this.model_expression = model_expression;
    }

}