





import java.util.List;
import java.util.ArrayList;

public class eJSL_CssBlock  {

    private String selector;





    private List<eJSL_KeyValuePair> ejsl_keyvaluepairs;




    private eJSL_Template ejsl_template;


    public eJSL_CssBlock(
        String selector    ) {
        this.selector = selector;
        this.ejsl_keyvaluepairs = new ArrayList<>();
    }

    public eJSL_CssBlock(
        String selector        ArrayList<eJSL_KeyValuePair> ejsl_keyvaluepairs    ) {
        this.selector = selector;
        this.ejsl_keyvaluepairs = ejsl_keyvaluepairs;
    }

    public String getSelector() {
        return selector;
    }

    public void setSelector(String selector) {
        this.selector = selector;
    }

    public List<eJSL_KeyValuePair> getEjsl_keyvaluepairs() {
        return ejsl_keyvaluepairs;
    }

    public void addEjsl_keyvaluepair(Ejsl_keyvaluepair ejsl_keyvaluepair) {
        this.ejsl_keyvaluepairs.add(ejsl_keyvaluepair);
    }
    public eJSL_Template getEjsl_template() {
        return ejsl_template;
    }

    public void setEjsl_template(eJSL_Template ejsl_template) {
        this.ejsl_template = ejsl_template;
    }

}