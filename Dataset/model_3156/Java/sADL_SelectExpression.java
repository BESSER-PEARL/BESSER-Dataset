





import java.util.List;
import java.util.ArrayList;

public class sADL_SelectExpression extends Expression {

    private boolean distinct;
    private String orderby;





    private sADL_Expression sadl_expression;




    private List<sADL_SadlResource> sadl_sadlresources;


    public sADL_SelectExpression(
        boolean distinct,        String orderby    ) {
        super(
        );
        this.distinct = distinct;
        this.orderby = orderby;
        this.sadl_sadlresources = new ArrayList<>();
    }

    public sADL_SelectExpression(
        boolean distinct,        String orderby        ArrayList<sADL_SadlResource> sadl_sadlresources    ) {
        this.distinct = distinct;
        this.orderby = orderby;
        this.sadl_sadlresources = sadl_sadlresources;
    }

    public boolean getDistinct() {
        return distinct;
    }

    public void setDistinct(boolean distinct) {
        this.distinct = distinct;
    }
    public String getOrderby() {
        return orderby;
    }

    public void setOrderby(String orderby) {
        this.orderby = orderby;
    }

    public sADL_Expression getSadl_expression() {
        return sadl_expression;
    }

    public void setSadl_expression(sADL_Expression sadl_expression) {
        this.sadl_expression = sadl_expression;
    }
    public List<sADL_SadlResource> getSadl_sadlresources() {
        return sadl_sadlresources;
    }

    public void addSadl_sadlresource(Sadl_sadlresource sadl_sadlresource) {
        this.sadl_sadlresources.add(sadl_sadlresource);
    }

}