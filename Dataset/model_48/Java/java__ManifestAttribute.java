





import java.util.List;
import java.util.ArrayList;

public class java__ManifestAttribute  {

    private String key;
    private String value;





    private java__Manifest java__manifest;


    public java__ManifestAttribute(
        String key,        String value    ) {
        this.key = key;
        this.value = value;
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

    public java__Manifest getJava__manifest() {
        return java__manifest;
    }

    public void setJava__manifest(java__Manifest java__manifest) {
        this.java__manifest = java__manifest;
    }

}