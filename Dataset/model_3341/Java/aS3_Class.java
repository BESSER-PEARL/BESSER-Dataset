





import java.util.List;
import java.util.ArrayList;

public class aS3_Class  {

    private String name;





    private List<aS3_Annotation> as3_annotations;




    private List<aS3_Interface> as3_interfaces;




    private List<aS3_Member> as3_members;




    private aS3_Modifier as3_modifier;




    private aS3_Class as3_class;


    public aS3_Class(
        String name    ) {
        this.name = name;
        this.as3_annotations = new ArrayList<>();
        this.as3_interfaces = new ArrayList<>();
        this.as3_members = new ArrayList<>();
    }

    public aS3_Class(
        String name        ArrayList<aS3_Annotation> as3_annotations,        ArrayList<aS3_Interface> as3_interfaces,        ArrayList<aS3_Member> as3_members    ) {
        this.name = name;
        this.as3_annotations = as3_annotations;
        this.as3_interfaces = as3_interfaces;
        this.as3_members = as3_members;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<aS3_Annotation> getAs3_annotations() {
        return as3_annotations;
    }

    public void addAs3_annotation(As3_annotation as3_annotation) {
        this.as3_annotations.add(as3_annotation);
    }
    public List<aS3_Interface> getAs3_interfaces() {
        return as3_interfaces;
    }

    public void addAs3_interface(As3_interface as3_interface) {
        this.as3_interfaces.add(as3_interface);
    }
    public List<aS3_Member> getAs3_members() {
        return as3_members;
    }

    public void addAs3_member(As3_member as3_member) {
        this.as3_members.add(as3_member);
    }
    public aS3_Modifier getAs3_modifier() {
        return as3_modifier;
    }

    public void setAs3_modifier(aS3_Modifier as3_modifier) {
        this.as3_modifier = as3_modifier;
    }
    public aS3_Class getAs3_class() {
        return as3_class;
    }

    public void setAs3_class(aS3_Class as3_class) {
        this.as3_class = as3_class;
    }

}