





import java.util.List;
import java.util.ArrayList;

public class pivot_Type extends NamedElement, TemplateableElement, ParameterableElement {

    private String instanceClassName;





    private pivot_Type pivot_type;




    private pivot_Property pivot_property;




    private pivot_DataType pivot_datatype;




    private List<pivot_Property> pivot_propertys;




    private pivot_Metaclass pivot_metaclass;




    private pivot_UnspecifiedType pivot_unspecifiedtype;




    private pivot_UnspecifiedType pivot_unspecifiedtype;


    public pivot_Type(
        String instanceClassName    ) {
        super(
        );
        this.instanceClassName = instanceClassName;
        this.pivot_propertys = new ArrayList<>();
    }

    public pivot_Type(
        String instanceClassName        ArrayList<pivot_Property> pivot_propertys    ) {
        this.instanceClassName = instanceClassName;
        this.pivot_propertys = pivot_propertys;
    }

    public String getInstanceclassname() {
        return instanceClassName;
    }

    public void setInstanceclassname(String instanceClassName) {
        this.instanceClassName = instanceClassName;
    }

    public pivot_Type getPivot_type() {
        return pivot_type;
    }

    public void setPivot_type(pivot_Type pivot_type) {
        this.pivot_type = pivot_type;
    }
    public pivot_Property getPivot_property() {
        return pivot_property;
    }

    public void setPivot_property(pivot_Property pivot_property) {
        this.pivot_property = pivot_property;
    }
    public pivot_DataType getPivot_datatype() {
        return pivot_datatype;
    }

    public void setPivot_datatype(pivot_DataType pivot_datatype) {
        this.pivot_datatype = pivot_datatype;
    }
    public List<pivot_Property> getPivot_propertys() {
        return pivot_propertys;
    }

    public void addPivot_property(Pivot_property pivot_property) {
        this.pivot_propertys.add(pivot_property);
    }
    public pivot_Metaclass getPivot_metaclass() {
        return pivot_metaclass;
    }

    public void setPivot_metaclass(pivot_Metaclass pivot_metaclass) {
        this.pivot_metaclass = pivot_metaclass;
    }
    public pivot_UnspecifiedType getPivot_unspecifiedtype() {
        return pivot_unspecifiedtype;
    }

    public void setPivot_unspecifiedtype(pivot_UnspecifiedType pivot_unspecifiedtype) {
        this.pivot_unspecifiedtype = pivot_unspecifiedtype;
    }
    public pivot_UnspecifiedType getPivot_unspecifiedtype() {
        return pivot_unspecifiedtype;
    }

    public void setPivot_unspecifiedtype(pivot_UnspecifiedType pivot_unspecifiedtype) {
        this.pivot_unspecifiedtype = pivot_unspecifiedtype;
    }

}