





import java.util.List;
import java.util.ArrayList;

public class XPath_Step extends LocatedElement {






    private XPath_Axis xpath_axis;




    private List<XPath_Predicate> xpath_predicates;


    public XPath_Step(
    ) {
        super(
        );
        this.xpath_predicates = new ArrayList<>();
    }

    public XPath_Step(
        ArrayList<XPath_Predicate> xpath_predicates    ) {
        this.xpath_predicates = xpath_predicates;
    }


    public XPath_Axis getXpath_axis() {
        return xpath_axis;
    }

    public void setXpath_axis(XPath_Axis xpath_axis) {
        this.xpath_axis = xpath_axis;
    }
    public List<XPath_Predicate> getXpath_predicates() {
        return xpath_predicates;
    }

    public void addXpath_predicate(Xpath_predicate xpath_predicate) {
        this.xpath_predicates.add(xpath_predicate);
    }

}