





import java.util.List;
import java.util.ArrayList;

public class model_ExpectedResult  {

    private String statusCode;
    private String contentType;
    private String responseBody;





    private model_ConfigExpectedResultPair model_configexpectedresultpair;


    public model_ExpectedResult(
        String statusCode,        String contentType,        String responseBody    ) {
        this.statusCode = statusCode;
        this.contentType = contentType;
        this.responseBody = responseBody;
    }


    public String getStatuscode() {
        return statusCode;
    }

    public void setStatuscode(String statusCode) {
        this.statusCode = statusCode;
    }
    public String getContenttype() {
        return contentType;
    }

    public void setContenttype(String contentType) {
        this.contentType = contentType;
    }
    public String getResponsebody() {
        return responseBody;
    }

    public void setResponsebody(String responseBody) {
        this.responseBody = responseBody;
    }

    public model_ConfigExpectedResultPair getModel_configexpectedresultpair() {
        return model_configexpectedresultpair;
    }

    public void setModel_configexpectedresultpair(model_ConfigExpectedResultPair model_configexpectedresultpair) {
        this.model_configexpectedresultpair = model_configexpectedresultpair;
    }

}