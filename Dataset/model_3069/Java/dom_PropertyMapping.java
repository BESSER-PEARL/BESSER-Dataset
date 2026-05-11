





import java.util.List;
import java.util.ArrayList;

public class dom_PropertyMapping  {

    private boolean toLeft;
    private boolean toRight;
    private boolean biDirectional;





    private dom_Attribute dom_attribute;




    private dom_Mapper dom_mapper;




    private dom_Attribute dom_attribute;


    public dom_PropertyMapping(
        boolean toLeft,        boolean toRight,        boolean biDirectional    ) {
        this.toLeft = toLeft;
        this.toRight = toRight;
        this.biDirectional = biDirectional;
    }


    public boolean getToleft() {
        return toLeft;
    }

    public void setToleft(boolean toLeft) {
        this.toLeft = toLeft;
    }
    public boolean getToright() {
        return toRight;
    }

    public void setToright(boolean toRight) {
        this.toRight = toRight;
    }
    public boolean getBidirectional() {
        return biDirectional;
    }

    public void setBidirectional(boolean biDirectional) {
        this.biDirectional = biDirectional;
    }

    public dom_Attribute getDom_attribute() {
        return dom_attribute;
    }

    public void setDom_attribute(dom_Attribute dom_attribute) {
        this.dom_attribute = dom_attribute;
    }
    public dom_Mapper getDom_mapper() {
        return dom_mapper;
    }

    public void setDom_mapper(dom_Mapper dom_mapper) {
        this.dom_mapper = dom_mapper;
    }
    public dom_Attribute getDom_attribute() {
        return dom_attribute;
    }

    public void setDom_attribute(dom_Attribute dom_attribute) {
        this.dom_attribute = dom_attribute;
    }

}