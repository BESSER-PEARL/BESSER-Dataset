





import java.util.List;
import java.util.ArrayList;

public class sADL_ExternalEquationStatement extends AbstractSadlEquation, SadlModelElement {

    private String location;
    private String uri;



    public sADL_ExternalEquationStatement(
        String location,        String uri    ) {
        super(
        );
        this.location = location;
        this.uri = uri;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }


}