





import java.util.List;
import java.util.ArrayList;

public class aml_ArgumentTemplate  {

    private String value;
    private String idRef;





    private aml_DiscoveryMethod aml_discoverymethod;




    private aml_Collection aml_collection;




    private aml_Argument aml_argument;


    public aml_ArgumentTemplate(
        String value,        String idRef    ) {
        this.value = value;
        this.idRef = idRef;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getIdref() {
        return idRef;
    }

    public void setIdref(String idRef) {
        this.idRef = idRef;
    }

    public aml_DiscoveryMethod getAml_discoverymethod() {
        return aml_discoverymethod;
    }

    public void setAml_discoverymethod(aml_DiscoveryMethod aml_discoverymethod) {
        this.aml_discoverymethod = aml_discoverymethod;
    }
    public aml_Collection getAml_collection() {
        return aml_collection;
    }

    public void setAml_collection(aml_Collection aml_collection) {
        this.aml_collection = aml_collection;
    }
    public aml_Argument getAml_argument() {
        return aml_argument;
    }

    public void setAml_argument(aml_Argument aml_argument) {
        this.aml_argument = aml_argument;
    }

}