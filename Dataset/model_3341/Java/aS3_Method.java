





import java.util.List;
import java.util.ArrayList;

public class aS3_Method  {

    private String anytype;
    private String name;





    private aS3_Block as3_block;




    private aS3_Modifier as3_modifier;




    private aS3_Member as3_member;




    private List<aS3_Parameter> as3_parameters;




    private aS3_EObject as3_eobject;




    private List<aS3_Annotation> as3_annotations;




    private aS3_AccessorRole as3_accessorrole;


    public aS3_Method(
        String anytype,        String name    ) {
        this.anytype = anytype;
        this.name = name;
        this.as3_parameters = new ArrayList<>();
        this.as3_annotations = new ArrayList<>();
    }

    public aS3_Method(
        String anytype,        String name        ArrayList<aS3_Parameter> as3_parameters,        ArrayList<aS3_Annotation> as3_annotations    ) {
        this.anytype = anytype;
        this.name = name;
        this.as3_parameters = as3_parameters;
        this.as3_annotations = as3_annotations;
    }

    public String getAnytype() {
        return anytype;
    }

    public void setAnytype(String anytype) {
        this.anytype = anytype;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public aS3_Block getAs3_block() {
        return as3_block;
    }

    public void setAs3_block(aS3_Block as3_block) {
        this.as3_block = as3_block;
    }
    public aS3_Modifier getAs3_modifier() {
        return as3_modifier;
    }

    public void setAs3_modifier(aS3_Modifier as3_modifier) {
        this.as3_modifier = as3_modifier;
    }
    public aS3_Member getAs3_member() {
        return as3_member;
    }

    public void setAs3_member(aS3_Member as3_member) {
        this.as3_member = as3_member;
    }
    public List<aS3_Parameter> getAs3_parameters() {
        return as3_parameters;
    }

    public void addAs3_parameter(As3_parameter as3_parameter) {
        this.as3_parameters.add(as3_parameter);
    }
    public aS3_EObject getAs3_eobject() {
        return as3_eobject;
    }

    public void setAs3_eobject(aS3_EObject as3_eobject) {
        this.as3_eobject = as3_eobject;
    }
    public List<aS3_Annotation> getAs3_annotations() {
        return as3_annotations;
    }

    public void addAs3_annotation(As3_annotation as3_annotation) {
        this.as3_annotations.add(as3_annotation);
    }
    public aS3_AccessorRole getAs3_accessorrole() {
        return as3_accessorrole;
    }

    public void setAs3_accessorrole(aS3_AccessorRole as3_accessorrole) {
        this.as3_accessorrole = as3_accessorrole;
    }

}