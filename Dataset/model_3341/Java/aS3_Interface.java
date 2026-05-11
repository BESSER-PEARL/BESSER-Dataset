





import java.util.List;
import java.util.ArrayList;

public class aS3_Interface  {

    private String access;
    private String name;





    private aS3_Interface as3_interface;




    private List<aS3_Annotation> as3_annotations;


    public aS3_Interface(
        String access,        String name    ) {
        this.access = access;
        this.name = name;
        this.as3_annotations = new ArrayList<>();
    }

    public aS3_Interface(
        String access,        String name        ArrayList<aS3_Annotation> as3_annotations    ) {
        this.access = access;
        this.name = name;
        this.as3_annotations = as3_annotations;
    }

    public String getAccess() {
        return access;
    }

    public void setAccess(String access) {
        this.access = access;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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