





import java.util.List;
import java.util.ArrayList;

public class dom_Operation extends DaoOperation, IDocumentable {

    private String expression;





    private dom_Service dom_service;




    private List<dom_Parameter> dom_parameters;




    private dom_Dao dom_dao;


    public dom_Operation(
        String expression    ) {
        super(
        );
        this.expression = expression;
        this.dom_parameters = new ArrayList<>();
    }

    public dom_Operation(
        String expression        ArrayList<dom_Parameter> dom_parameters    ) {
        this.expression = expression;
        this.dom_parameters = dom_parameters;
    }

    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }

    public dom_Service getDom_service() {
        return dom_service;
    }

    public void setDom_service(dom_Service dom_service) {
        this.dom_service = dom_service;
    }
    public List<dom_Parameter> getDom_parameters() {
        return dom_parameters;
    }

    public void addDom_parameter(Dom_parameter dom_parameter) {
        this.dom_parameters.add(dom_parameter);
    }
    public dom_Dao getDom_dao() {
        return dom_dao;
    }

    public void setDom_dao(dom_Dao dom_dao) {
        this.dom_dao = dom_dao;
    }

}