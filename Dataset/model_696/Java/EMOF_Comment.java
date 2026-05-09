





import java.util.List;
import java.util.ArrayList;

public class EMOF_Comment extends Element {

    private String body;



    public EMOF_Comment(
        String body    ) {
        super(
        );
        this.body = body;
    }


    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }


}