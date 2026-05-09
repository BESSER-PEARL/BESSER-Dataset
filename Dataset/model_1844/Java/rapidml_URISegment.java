





import java.util.List;
import java.util.ArrayList;

public class rapidml_URISegment extends HasStringValue {

    private String name;





    private rapidml_URI rapidml_uri;


    public rapidml_URISegment(
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

    public rapidml_URI getRapidml_uri() {
        return rapidml_uri;
    }

    public void setRapidml_uri(rapidml_URI rapidml_uri) {
        this.rapidml_uri = rapidml_uri;
    }

}