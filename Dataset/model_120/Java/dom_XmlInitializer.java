





import java.util.List;
import java.util.ArrayList;

public class dom_XmlInitializer extends Expression {






    private List<dom_XmlFragment> dom_xmlfragments;


    public dom_XmlInitializer(
    ) {
        super(
        );
        this.dom_xmlfragments = new ArrayList<>();
    }

    public dom_XmlInitializer(
        ArrayList<dom_XmlFragment> dom_xmlfragments    ) {
        this.dom_xmlfragments = dom_xmlfragments;
    }


    public List<dom_XmlFragment> getDom_xmlfragments() {
        return dom_xmlfragments;
    }

    public void addDom_xmlfragment(Dom_xmlfragment dom_xmlfragment) {
        this.dom_xmlfragments.add(dom_xmlfragment);
    }

}