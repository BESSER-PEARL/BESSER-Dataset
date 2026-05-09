





import java.util.List;
import java.util.ArrayList;

public class DOM_WildcardType extends Type {

    private String upperBound;





    private DOM_Type dom_type;


    public DOM_WildcardType(
        String upperBound    ) {
        super(
        );
        this.upperBound = upperBound;
    }


    public String getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(String upperBound) {
        this.upperBound = upperBound;
    }

    public DOM_Type getDom_type() {
        return dom_type;
    }

    public void setDom_type(DOM_Type dom_type) {
        this.dom_type = dom_type;
    }

}