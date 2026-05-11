





import java.util.List;
import java.util.ArrayList;

public class dom_AggregateFunction extends Expression {

    private boolean distinct;
    private String from_;
    private String function;
    private boolean all;





    private dom_Expression dom_expression;




    private dom_CollectionFunction dom_collectionfunction;


    public dom_AggregateFunction(
        boolean distinct,        String from_,        String function,        boolean all    ) {
        super(
        );
        this.distinct = distinct;
        this.from_ = from_;
        this.function = function;
        this.all = all;
    }


    public boolean getDistinct() {
        return distinct;
    }

    public void setDistinct(boolean distinct) {
        this.distinct = distinct;
    }
    public String getFrom_() {
        return from_;
    }

    public void setFrom_(String from_) {
        this.from_ = from_;
    }
    public String getFunction() {
        return function;
    }

    public void setFunction(String function) {
        this.function = function;
    }
    public boolean getAll() {
        return all;
    }

    public void setAll(boolean all) {
        this.all = all;
    }

    public dom_Expression getDom_expression() {
        return dom_expression;
    }

    public void setDom_expression(dom_Expression dom_expression) {
        this.dom_expression = dom_expression;
    }
    public dom_CollectionFunction getDom_collectionfunction() {
        return dom_collectionfunction;
    }

    public void setDom_collectionfunction(dom_CollectionFunction dom_collectionfunction) {
        this.dom_collectionfunction = dom_collectionfunction;
    }

}