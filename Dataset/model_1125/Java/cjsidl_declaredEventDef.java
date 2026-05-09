





import java.util.List;
import java.util.ArrayList;

public class cjsidl_declaredEventDef  {

    private String comment;
    private String name;





    private cjsidl_eventDef cjsidl_eventdef;




    private cjsidl_scopedEventType cjsidl_scopedeventtype;


    public cjsidl_declaredEventDef(
        String comment,        String name    ) {
        this.comment = comment;
        this.name = name;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cjsidl_eventDef getCjsidl_eventdef() {
        return cjsidl_eventdef;
    }

    public void setCjsidl_eventdef(cjsidl_eventDef cjsidl_eventdef) {
        this.cjsidl_eventdef = cjsidl_eventdef;
    }
    public cjsidl_scopedEventType getCjsidl_scopedeventtype() {
        return cjsidl_scopedeventtype;
    }

    public void setCjsidl_scopedeventtype(cjsidl_scopedEventType cjsidl_scopedeventtype) {
        this.cjsidl_scopedeventtype = cjsidl_scopedeventtype;
    }

}