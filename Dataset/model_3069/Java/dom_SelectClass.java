





import java.util.List;
import java.util.ArrayList;

public class dom_SelectClass extends SelectStatement {

    private String class_;





    private List<dom_Expression> dom_expressions;


    public dom_SelectClass(
        String class_    ) {
        super(
        );
        this.class_ = class_;
        this.dom_expressions = new ArrayList<>();
    }

    public dom_SelectClass(
        String class_        ArrayList<dom_Expression> dom_expressions    ) {
        this.class_ = class_;
        this.dom_expressions = dom_expressions;
    }

    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }

    public List<dom_Expression> getDom_expressions() {
        return dom_expressions;
    }

    public void addDom_expression(Dom_expression dom_expression) {
        this.dom_expressions.add(dom_expression);
    }

}