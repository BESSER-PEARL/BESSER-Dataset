





import java.util.List;
import java.util.ArrayList;

public class Java_ManifestEntry  {

    private String name;





    private Java_Manifest java_manifest;




    private List<Java_ManifestAttribute> java_manifestattributes;


    public Java_ManifestEntry(
        String name    ) {
        this.name = name;
        this.java_manifestattributes = new ArrayList<>();
    }

    public Java_ManifestEntry(
        String name        ArrayList<Java_ManifestAttribute> java_manifestattributes    ) {
        this.name = name;
        this.java_manifestattributes = java_manifestattributes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Java_Manifest getJava_manifest() {
        return java_manifest;
    }

    public void setJava_manifest(Java_Manifest java_manifest) {
        this.java_manifest = java_manifest;
    }
    public List<Java_ManifestAttribute> getJava_manifestattributes() {
        return java_manifestattributes;
    }

    public void addJava_manifestattribute(Java_manifestattribute java_manifestattribute) {
        this.java_manifestattributes.add(java_manifestattribute);
    }

}