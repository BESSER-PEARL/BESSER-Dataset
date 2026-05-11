





import java.util.List;
import java.util.ArrayList;

public class classmodel_Operation extends Feature {

    private boolean static;
    private String body;



    public classmodel_Operation(
        boolean static,        String body    ) {
        super(
        );
        this.static = static;
        this.body = body;
    }


    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }


}