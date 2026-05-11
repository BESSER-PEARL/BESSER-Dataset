





import java.util.List;
import java.util.ArrayList;

public class aS3_MemberVariableDeclaration  {

    private String name;
    private String anytype;





    private aS3_EObject as3_eobject;




    private List<aS3_Annotation> as3_annotations;




    private aS3_Modifier as3_modifier;




    private aS3_Member as3_member;


    public aS3_MemberVariableDeclaration(
        String name,        String anytype    ) {
        this.name = name;
        this.anytype = anytype;
        this.as3_annotations = new ArrayList<>();
    }

    public aS3_MemberVariableDeclaration(
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
    public List<aS3_Annotation> getAs3_annotations() {
        return as3_annotations;
    }

    public void addAs3_annotation(As3_annotation as3_annotation) {
        this.as3_annotations.add(as3_annotation);
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

}