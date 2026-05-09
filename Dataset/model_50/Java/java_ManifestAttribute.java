





import java.util.List;
import java.util.ArrayList;

public class java_ManifestAttribute  {

    private String key;
    private String value;





    private java_Manifest java_manifest;


    public java_ManifestAttribute(
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

    public java_Manifest getJava_manifest() {
        return java_manifest;
    }

    public void setJava_manifest(java_Manifest java_manifest) {
        this.java_manifest = java_manifest;
    }

}