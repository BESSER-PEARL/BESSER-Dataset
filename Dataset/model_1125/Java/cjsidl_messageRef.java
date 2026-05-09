





import java.util.List;
import java.util.ArrayList;

public class cjsidl_messageRef  {

    private String name;
    private String comment;





    private cjsidl_messages cjsidl_messages;




    private cjsidl_messageDef cjsidl_messagedef;


    public cjsidl_messageRef(
        String name,        String comment    ) {
        this.name = name;
        this.comment = comment;
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

    public cjsidl_messages getCjsidl_messages() {
        return cjsidl_messages;
    }

    public void setCjsidl_messages(cjsidl_messages cjsidl_messages) {
        this.cjsidl_messages = cjsidl_messages;
    }
    public cjsidl_messageDef getCjsidl_messagedef() {
        return cjsidl_messagedef;
    }

    public void setCjsidl_messagedef(cjsidl_messageDef cjsidl_messagedef) {
        this.cjsidl_messagedef = cjsidl_messagedef;
    }

}