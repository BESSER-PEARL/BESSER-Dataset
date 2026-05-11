





import java.util.List;
import java.util.ArrayList;

public class aS3_InterfaceMethod  {

    private String name;
    private String anytype;





    private aS3_EObject as3_eobject;




    private aS3_Interface as3_interface;




    private List<aS3_Annotation> as3_annotations;


    public aS3_InterfaceMethod(
        String name,        String anytype    ) {
        this.name = name;
        this.anytype = anytype;
        this.as3_annotations = new ArrayList<>();
    }

    public aS3_InterfaceMethod(
        String name,        String anytype        ArrayList<aS3_Annotation> as3_annotations    ) {
        this.name = name;
        this.anytype = anytype;
        this.as3_annotations = as3_annotations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAnytype() {
        return anytype;
    }

    public void setAnytype(String anytype) {
        this.anytype = anytype;
    }

    public aS3_EObject getAs3_eobject() {
        return as3_eobject;
    }

    public void setAs3_eobject(aS3_EObject as3_eobject) {
        this.as3_eobject = as3_eobject;
    }
    public aS3_Interface getAs3_interface() {
        return as3_interface;
    }

    public void setAs3_interface(aS3_Interface as3_interface) {
        this.as3_interface = as3_interface;
    }
    public List<aS3_Annotation> getAs3_annotations() {
        return as3_annotations;
    }

    public void addAs3_annotation(As3_annotation as3_annotation) {
        this.as3_annotations.add(as3_annotation);
    }

}