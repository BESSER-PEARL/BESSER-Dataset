





import java.util.List;
import java.util.ArrayList;

public class XPath_PathExpression extends Expression {

    private String isAbsolute;





    private List<XPath_Step> xpath_steps;


    public XPath_PathExpression(
        String isAbsolute    ) {
        super(
        );
        this.isAbsolute = isAbsolute;
        this.xpath_steps = new ArrayList<>();
    }

    public XPath_PathExpression(
        String isAbsolute        ArrayList<XPath_Step> xpath_steps    ) {
        this.isAbsolute = isAbsolute;
        this.xpath_steps = xpath_steps;
    }

    public String getIsabsolute() {
        return isAbsolute;
    }

    public void setIsabsolute(String isAbsolute) {
        this.isAbsolute = isAbsolute;
    }

    public List<XPath_Step> getXpath_steps() {
        return xpath_steps;
    }

    public void addXpath_step(Xpath_step xpath_step) {
        this.xpath_steps.add(xpath_step);
    }

}