





import java.util.List;
import java.util.ArrayList;

public class textlink_TextLocation extends TraceLinkEnd {

    private String resource;





    private textlink_TraceLink textlink_tracelink;


    public textlink_TextLocation(
        String resource    ) {
        super(
        );
        this.resource = resource;
    }


    public String getResource() {
        return resource;
    }

    public void setResource(String resource) {
        this.resource = resource;
    }

    public textlink_TraceLink getTextlink_tracelink() {
        return textlink_tracelink;
    }

    public void setTextlink_tracelink(textlink_TraceLink textlink_tracelink) {
        this.textlink_tracelink = textlink_tracelink;
    }

}