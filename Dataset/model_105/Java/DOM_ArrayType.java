





import java.util.List;
import java.util.ArrayList;

public class DOM_ArrayType extends Type {

    private String dimensions;





    private DOM_ArrayCreation dom_arraycreation;




    private DOM_Type dom_type;




    private DOM_Type dom_type;


    public DOM_ArrayType(
        String dimensions    ) {
        super(
        );
        this.dimensions = dimensions;
    }


    public String getDimensions() {
        return dimensions;
    }

    public void setDimensions(String dimensions) {
        this.dimensions = dimensions;
    }

    public DOM_ArrayCreation getDom_arraycreation() {
        return dom_arraycreation;
    }

    public void setDom_arraycreation(DOM_ArrayCreation dom_arraycreation) {
        this.dom_arraycreation = dom_arraycreation;
    }
    public DOM_Type getDom_type() {
        return dom_type;
    }

    public void setDom_type(DOM_Type dom_type) {
        this.dom_type = dom_type;
    }
    public DOM_Type getDom_type() {
        return dom_type;
    }

    public void setDom_type(DOM_Type dom_type) {
        this.dom_type = dom_type;
    }

}