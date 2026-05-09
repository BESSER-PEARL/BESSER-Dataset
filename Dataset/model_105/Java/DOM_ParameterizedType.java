





import java.util.List;
import java.util.ArrayList;

public class DOM_ParameterizedType extends Type {






    private List<DOM_Type> dom_types;




    private DOM_Type dom_type;


    public DOM_ParameterizedType(
    ) {
        super(
        );
        this.dom_types = new ArrayList<>();
    }

    public DOM_ParameterizedType(
        ArrayList<DOM_Type> dom_types    ) {
        this.dom_types = dom_types;
    }


    public List<DOM_Type> getDom_types() {
        return dom_types;
    }

    public void addDom_type(Dom_type dom_type) {
        this.dom_types.add(dom_type);
    }
    public DOM_Type getDom_type() {
        return dom_type;
    }

    public void setDom_type(DOM_Type dom_type) {
        this.dom_type = dom_type;
    }

}