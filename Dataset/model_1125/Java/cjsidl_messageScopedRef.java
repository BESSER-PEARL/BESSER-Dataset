





import java.util.List;
import java.util.ArrayList;

public class cjsidl_messageScopedRef  {

    private String name;
    private String comment;





    private cjsidl_EObject cjsidl_eobject;




    private cjsidl_messageDef cjsidl_messagedef;




    private cjsidl_messages cjsidl_messages;




    private List<cjsidl_EObject> cjsidl_eobjects;


    public cjsidl_messageScopedRef(
        String name,        String comment    ) {
        this.name = name;
        this.comment = comment;
        this.cjsidl_eobjects = new ArrayList<>();
    }

    public cjsidl_messageScopedRef(
        String name,        String comment        ArrayList<cjsidl_EObject> cjsidl_eobjects    ) {
        this.name = name;
        this.comment = comment;
        this.cjsidl_eobjects = cjsidl_eobjects;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public cjsidl_EObject getCjsidl_eobject() {
        return cjsidl_eobject;
    }

    public void setCjsidl_eobject(cjsidl_EObject cjsidl_eobject) {
        this.cjsidl_eobject = cjsidl_eobject;
    }
    public cjsidl_messageDef getCjsidl_messagedef() {
        return cjsidl_messagedef;
    }

    public void setCjsidl_messagedef(cjsidl_messageDef cjsidl_messagedef) {
        this.cjsidl_messagedef = cjsidl_messagedef;
    }
    public cjsidl_messages getCjsidl_messages() {
        return cjsidl_messages;
    }

    public void setCjsidl_messages(cjsidl_messages cjsidl_messages) {
        this.cjsidl_messages = cjsidl_messages;
    }
    public List<cjsidl_EObject> getCjsidl_eobjects() {
        return cjsidl_eobjects;
    }

    public void addCjsidl_eobject(Cjsidl_eobject cjsidl_eobject) {
        this.cjsidl_eobjects.add(cjsidl_eobject);
    }

}