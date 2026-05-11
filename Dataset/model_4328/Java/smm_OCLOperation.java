





import java.util.List;
import java.util.ArrayList;

public class smm_OCLOperation extends AbstractMeasureElement {

    private String context;
    private String body;



    public smm_OCLOperation(
        String context,        String body    ) {
        super(
        );
        this.context = context;
        this.body = body;
    }


    public String getContext() {
        return context;
    }

    public void setContext(String context) {
        this.context = context;
    }
    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }


}