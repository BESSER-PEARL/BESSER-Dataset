





import java.util.List;
import java.util.ArrayList;

public class domain_KeyValuePair  {

    private String key;
    private String value;
    private String uid;





    private domain_HashProperty domain_hashproperty;


    public domain_KeyValuePair(
        String key,        String value,        String uid    ) {
        this.key = key;
        this.value = value;
        this.uid = uid;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public domain_HashProperty getDomain_hashproperty() {
        return domain_hashproperty;
    }

    public void setDomain_hashproperty(domain_HashProperty domain_hashproperty) {
        this.domain_hashproperty = domain_hashproperty;
    }

}