





import java.util.List;
import java.util.ArrayList;

public class documentation_Link extends NamedElement, Fragment {

    private String uri;



    public documentation_Link(
        String uri    ) {
        super(
        );
        this.uri = uri;
    }


    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }


}