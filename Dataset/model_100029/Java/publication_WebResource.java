





import java.util.List;
import java.util.ArrayList;

public class publication_WebResource extends BiblioReference {

    private String uRL;



    public publication_WebResource(
        String uRL    ) {
        super(
        );
        this.uRL = uRL;
    }


    public String getUrl() {
        return uRL;
    }

    public void setUrl(String uRL) {
        this.uRL = uRL;
    }


}