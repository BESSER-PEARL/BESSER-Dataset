





import java.util.List;
import java.util.ArrayList;

public class Java_ManifestAttribute  {

    private String value;
    private String key;





    private Java_Manifest java_manifest;


    public Java_ManifestAttribute(
        String value,        String key    ) {
        this.value = value;
        this.key = key;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public Java_Manifest getJava_manifest() {
        return java_manifest;
    }

    public void setJava_manifest(Java_Manifest java_manifest) {
        this.java_manifest = java_manifest;
    }

}