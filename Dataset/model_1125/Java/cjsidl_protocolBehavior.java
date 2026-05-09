





import java.util.List;
import java.util.ArrayList;

public class cjsidl_protocolBehavior  {

    private String stateless;
    private String comment;



    public cjsidl_protocolBehavior(
        String stateless,        String comment    ) {
        this.stateless = stateless;
        this.comment = comment;
    }


    public String getStateless() {
        return stateless;
    }

    public void setStateless(String stateless) {
        this.stateless = stateless;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }


}