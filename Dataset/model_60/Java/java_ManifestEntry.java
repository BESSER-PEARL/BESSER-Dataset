





import java.util.List;
import java.util.ArrayList;

public class java_ManifestEntry  {

    private String name;





    private List<java_ManifestAttribute> java_manifestattributes;




    private java_Manifest java_manifest;


    public java_ManifestEntry(
        String name    ) {
        this.name = name;
        this.java_manifestattributes = new ArrayList<>();
    }

    public java_ManifestEntry(
        String name        ArrayList<java_ManifestAttribute> java_manifestattributes    ) {
        this.name = name;
        this.java_manifestattributes = java_manifestattributes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<java_ManifestAttribute> getJava_manifestattributes() {
        return java_manifestattributes;
    }

    public void addJava_manifestattribute(Java_manifestattribute java_manifestattribute) {
        this.java_manifestattributes.add(java_manifestattribute);
    }
    public java_Manifest getJava_manifest() {
        return java_manifest;
    }

    public void setJava_manifest(java_Manifest java_manifest) {
        this.java_manifest = java_manifest;
    }

}