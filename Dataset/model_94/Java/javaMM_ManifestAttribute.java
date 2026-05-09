





import java.util.List;
import java.util.ArrayList;

public class javaMM_ManifestAttribute  {

    private String key;
    private String value;





    private javaMM_Manifest javamm_manifest;


    public javaMM_ManifestAttribute(
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

    public javaMM_Manifest getJavamm_manifest() {
        return javamm_manifest;
    }

    public void setJavamm_manifest(javaMM_Manifest javamm_manifest) {
        this.javamm_manifest = javamm_manifest;
    }

}