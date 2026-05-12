





import java.util.List;
import java.util.ArrayList;

public class sparql_UsingGraph  {

    private String uri;
    private boolean named;



    public sparql_UsingGraph(
        String uri,        boolean named    ) {
        this.uri = uri;
        this.named = named;
    }


    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }
    public boolean getNamed() {
        return named;
    }

    public void setNamed(boolean named) {
        this.named = named;
    }


}