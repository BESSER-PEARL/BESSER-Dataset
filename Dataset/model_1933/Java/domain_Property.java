





import java.util.List;
import java.util.ArrayList;

public class domain_Property  {

    private String uid;
    private String value;
    private String fakeName;





    private domain_Configuration domain_configuration;




    private domain_ConfigVariable domain_configvariable;


    public domain_Property(
        String uid,        String value,        String fakeName    ) {
        this.uid = uid;
        this.value = value;
        this.fakeName = fakeName;
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
    public String getFakename() {
        return fakeName;
    }

    public void setFakename(String fakeName) {
        this.fakeName = fakeName;
    }

    public domain_Configuration getDomain_configuration() {
        return domain_configuration;
    }

    public void setDomain_configuration(domain_Configuration domain_configuration) {
        this.domain_configuration = domain_configuration;
    }
    public domain_ConfigVariable getDomain_configvariable() {
        return domain_configvariable;
    }

    public void setDomain_configvariable(domain_ConfigVariable domain_configvariable) {
        this.domain_configvariable = domain_configvariable;
    }

}