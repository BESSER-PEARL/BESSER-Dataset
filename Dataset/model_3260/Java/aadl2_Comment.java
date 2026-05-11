





import java.util.List;
import java.util.ArrayList;

public class aadl2_Comment extends Element {

    private String body;



    public aadl2_Comment(
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