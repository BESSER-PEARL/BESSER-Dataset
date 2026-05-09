





import java.util.List;
import java.util.ArrayList;

public class java_Manifest  {






    private List<java_ManifestEntry> java_manifestentrys;




    private List<java_ManifestAttribute> java_manifestattributes;


    public java_Manifest(
    ) {
        this.java_manifestentrys = new ArrayList<>();
        this.java_manifestattributes = new ArrayList<>();
    }

    public java_Manifest(
        ArrayList<java_ManifestEntry> java_manifestentrys,        ArrayList<java_ManifestAttribute> java_manifestattributes    ) {
        this.java_manifestentrys = java_manifestentrys;
        this.java_manifestattributes = java_manifestattributes;
    }


    public List<java_ManifestEntry> getJava_manifestentrys() {
        return java_manifestentrys;
    }

    public void addJava_manifestentry(Java_manifestentry java_manifestentry) {
        this.java_manifestentrys.add(java_manifestentry);
    }
    public List<java_ManifestAttribute> getJava_manifestattributes() {
        return java_manifestattributes;
    }

    public void addJava_manifestattribute(Java_manifestattribute java_manifestattribute) {
        this.java_manifestattributes.add(java_manifestattribute);
    }

}