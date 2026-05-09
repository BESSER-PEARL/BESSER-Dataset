





import java.util.List;
import java.util.ArrayList;

public class domain_QueryVariable  {

    private String uid;
    private String value;





    private domain_QueryParameter domain_queryparameter;




    private domain_Query domain_query;


    public domain_QueryVariable(
        String uid,        String value    ) {
        this.uid = uid;
        this.value = value;
    }


    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public domain_QueryParameter getDomain_queryparameter() {
        return domain_queryparameter;
    }

    public void setDomain_queryparameter(domain_QueryParameter domain_queryparameter) {
        this.domain_queryparameter = domain_queryparameter;
    }
    public domain_Query getDomain_query() {
        return domain_query;
    }

    public void setDomain_query(domain_Query domain_query) {
        this.domain_query = domain_query;
    }

}