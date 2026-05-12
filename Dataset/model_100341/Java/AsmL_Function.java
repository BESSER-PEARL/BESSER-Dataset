





import java.util.List;
import java.util.ArrayList;

public class AsmL_Function extends AsmLElement {

    private String name;





    private Body body;


    public AsmL_Function(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Body getBody() {
        return body;
    }

    public void setBody(Body body) {
        this.body = body;
    }

}