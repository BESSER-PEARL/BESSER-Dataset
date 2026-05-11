





import java.util.List;
import java.util.ArrayList;

public class model_Config  {

    private String requestBody;
    private String contentType;
    private String name;
    private String httpVerb;
    private String requestURL;





    private model_Response model_response;


    public model_Config(
        String requestBody,        String contentType,        String name,        String httpVerb,        String requestURL    ) {
        this.requestBody = requestBody;
        this.contentType = contentType;
        this.name = name;
        this.httpVerb = httpVerb;
        this.requestURL = requestURL;
    }


    public String getRequestbody() {
        return requestBody;
    }

    public void setRequestbody(String requestBody) {
        this.requestBody = requestBody;
    }
    public String getContenttype() {
        return contentType;
    }

    public void setContenttype(String contentType) {
        this.contentType = contentType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getHttpverb() {
        return httpVerb;
    }

    public void setHttpverb(String httpVerb) {
        this.httpVerb = httpVerb;
    }
    public String getRequesturl() {
        return requestURL;
    }

    public void setRequesturl(String requestURL) {
        this.requestURL = requestURL;
    }

    public model_Response getModel_response() {
        return model_response;
    }

    public void setModel_response(model_Response model_response) {
        this.model_response = model_response;
    }

}