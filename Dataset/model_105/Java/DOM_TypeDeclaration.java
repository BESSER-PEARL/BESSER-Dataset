





import java.util.List;
import java.util.ArrayList;

public class DOM_TypeDeclaration extends AbstractTypeDeclaration {

    private String interface;





    private List<DOM_Type> dom_types;




    private List<DOM_TypeParameter> dom_typeparameters;




    private DOM_Type dom_type;


    public DOM_TypeDeclaration(
        String interface    ) {
        super(
        );
        this.interface = interface;
        this.dom_types = new ArrayList<>();
        this.dom_typeparameters = new ArrayList<>();
    }

    public DOM_TypeDeclaration(
        String interface        ArrayList<DOM_Type> dom_types,        ArrayList<DOM_TypeParameter> dom_typeparameters    ) {
        this.interface = interface;
        this.dom_types = dom_types;
        this.dom_typeparameters = dom_typeparameters;
    }

    public String getInterface() {
        return interface;
    }

    public void setInterface(String interface) {
        this.interface = interface;
    }

    public List<DOM_Type> getDom_types() {
        return dom_types;
    }

    public void addDom_type(Dom_type dom_type) {
        this.dom_types.add(dom_type);
    }
    public List<DOM_TypeParameter> getDom_typeparameters() {
        return dom_typeparameters;
    }

    public void addDom_typeparameter(Dom_typeparameter dom_typeparameter) {
        this.dom_typeparameters.add(dom_typeparameter);
    }
    public DOM_Type getDom_type() {
        return dom_type;
    }

    public void setDom_type(DOM_Type dom_type) {
        this.dom_type = dom_type;
    }

}