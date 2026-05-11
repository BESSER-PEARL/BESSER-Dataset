





import java.util.List;
import java.util.ArrayList;

public class aml_End  {

    private String scheme;
    private String value;





    private aml_DocumentRoot aml_documentroot;


    public aml_End(
        String scheme,        String value    ) {
        this.scheme = scheme;
        this.value = value;
    }


    public String getScheme() {
        return scheme;
    }

    public void setScheme(String scheme) {
        this.scheme = scheme;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public aml_DocumentRoot getAml_documentroot() {
        return aml_documentroot;
    }

    public void setAml_documentroot(aml_DocumentRoot aml_documentroot) {
        this.aml_documentroot = aml_documentroot;
    }

}