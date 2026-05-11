





import java.util.List;
import java.util.ArrayList;

public class XPath_FunctionCallExp extends Expression, NamedElement {






    private List<XPath_Expression> xpath_expressions;


    public XPath_FunctionCallExp(
    ) {
        super(
        );
        this.xpath_expressions = new ArrayList<>();
    }

    public XPath_FunctionCallExp(
        ArrayList<XPath_Expression> xpath_expressions    ) {
        this.xpath_expressions = xpath_expressions;
    }


    public List<XPath_Expression> getXpath_expressions() {
        return xpath_expressions;
    }

    public void addXpath_expression(Xpath_expression xpath_expression) {
        this.xpath_expressions.add(xpath_expression);
    }

}