





import java.util.List;
import java.util.ArrayList;

public class sadl_SelectExpression extends Expression {

    private String orderby;
    private String distinct;
    private String allVars;





    private sadl_VariableList sadl_variablelist;


    public sadl_SelectExpression(
        String orderby,        String distinct,        String allVars    ) {
        super(
        );
        this.orderby = orderby;
        this.distinct = distinct;
        this.allVars = allVars;
    }


    public String getOrderby() {
        return orderby;
    }

    public void setOrderby(String orderby) {
        this.orderby = orderby;
    }
    public String getDistinct() {
        return distinct;
    }

    public void setDistinct(String distinct) {
        this.distinct = distinct;
    }
    public String getAllvars() {
        return allVars;
    }

    public void setAllvars(String allVars) {
        this.allVars = allVars;
    }

    public sadl_VariableList getSadl_variablelist() {
        return sadl_variablelist;
    }

    public void setSadl_variablelist(sadl_VariableList sadl_variablelist) {
        this.sadl_variablelist = sadl_variablelist;
    }

}