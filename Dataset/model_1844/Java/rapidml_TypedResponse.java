





import java.util.List;
import java.util.ArrayList;

public class rapidml_TypedResponse extends TypedMessage {

    private int statusCode;





    private rapidml_Method rapidml_method;




    private rapidml_Method rapidml_method;




    private rapidml_SecurityScheme rapidml_securityscheme;


    public rapidml_TypedResponse(
        int statusCode    ) {
        super(
        );
        this.statusCode = statusCode;
    }


    public int getStatuscode() {
        return statusCode;
    }

    public void setStatuscode(int statusCode) {
        this.statusCode = statusCode;
    }

    public rapidml_Method getRapidml_method() {
        return rapidml_method;
    }

    public void setRapidml_method(rapidml_Method rapidml_method) {
        this.rapidml_method = rapidml_method;
    }
    public rapidml_Method getRapidml_method() {
        return rapidml_method;
    }

    public void setRapidml_method(rapidml_Method rapidml_method) {
        this.rapidml_method = rapidml_method;
    }
    public rapidml_SecurityScheme getRapidml_securityscheme() {
        return rapidml_securityscheme;
    }

    public void setRapidml_securityscheme(rapidml_SecurityScheme rapidml_securityscheme) {
        this.rapidml_securityscheme = rapidml_securityscheme;
    }

}