





import java.util.List;
import java.util.ArrayList;

public class model_Response  {

    private String responseBody;
    private String contentType;
    private String responseTime;
    private String statusCode;



    public model_Response(
        String responseBody,        String contentType,        String responseTime,        String statusCode    ) {
        this.responseBody = responseBody;
        this.contentType = contentType;
        this.responseTime = responseTime;
        this.statusCode = statusCode;
    }


    public String getResponsebody() {
        return responseBody;
    }

    public void setResponsebody(String responseBody) {
        this.responseBody = responseBody;
    }
    public String getContenttype() {
        return contentType;
    }

    public void setContenttype(String contentType) {
        this.contentType = contentType;
    }
    public String getResponsetime() {
        return responseTime;
    }

    public void setResponsetime(String responseTime) {
        this.responseTime = responseTime;
    }
    public String getStatuscode() {
        return statusCode;
    }

    public void setStatuscode(String statusCode) {
        this.statusCode = statusCode;
    }


}