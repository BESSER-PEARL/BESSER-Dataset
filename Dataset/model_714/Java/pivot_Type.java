





import java.util.List;
import java.util.ArrayList;

public class pivot_Type extends ParameterableElement, TemplateableElement, NamedElement {

    private String instanceClassName;





    private pivot_TypedElement pivot_typedelement;




    private pivot_Type pivot_type;




    private pivot_TypeExp pivot_typeexp;


    public pivot_Type(
        String instanceClassName    ) {
        super(
        );
        this.instanceClassName = instanceClassName;
    }


    public String getInstanceclassname() {
        return instanceClassName;
    }

    public void setInstanceclassname(String instanceClassName) {
        this.instanceClassName = instanceClassName;
    }

    public pivot_TypedElement getPivot_typedelement() {
        return pivot_typedelement;
    }

    public void setPivot_typedelement(pivot_TypedElement pivot_typedelement) {
        this.pivot_typedelement = pivot_typedelement;
    }
    public pivot_Type getPivot_type() {
        return pivot_type;
    }

    public void setPivot_type(pivot_Type pivot_type) {
        this.pivot_type = pivot_type;
    }
    public pivot_TypeExp getPivot_typeexp() {
        return pivot_typeexp;
    }

    public void setPivot_typeexp(pivot_TypeExp pivot_typeexp) {
        this.pivot_typeexp = pivot_typeexp;
    }

}