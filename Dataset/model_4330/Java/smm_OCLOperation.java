





import java.util.List;
import java.util.ArrayList;

public class smm_OCLOperation extends AbstractMeasureElement {

    private String body;
    private String context;



    public smm_OCLOperation(
        String body,        String context    ) {
        super(
        );
        this.body = body;
        this.context = context;
    }


    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }
    public String getContext() {
        return context;
    }

    public void setContext(String context) {
        this.context = context;
    }


}