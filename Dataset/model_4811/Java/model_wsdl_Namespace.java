





import java.util.List;
import java.util.ArrayList;

public class model_wsdl_Namespace  {

    private String prefix;
    private String URI;



    public model_wsdl_Namespace(
        String prefix,        String URI    ) {
        this.prefix = prefix;
        this.URI = URI;
    }


    public String getPrefix() {
        return prefix;
    }

    public void setPrefix(String prefix) {
        this.prefix = prefix;
    }
    public String getUri() {
        return URI;
    }

    public void setUri(String URI) {
        this.URI = URI;
    }


}