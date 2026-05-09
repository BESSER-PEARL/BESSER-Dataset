





import java.util.List;
import java.util.ArrayList;

public class java_Manifest  {






    private List<java_ManifestAttribute> java_manifestattributes;




    private java_Archive java_archive;




    private List<java_ManifestEntry> java_manifestentrys;


    public java_Manifest(
    ) {
        this.java_manifestattributes = new ArrayList<>();
        this.java_manifestentrys = new ArrayList<>();
    }

    public java_Manifest(
        ArrayList<java_ManifestAttribute> java_manifestattributes,        ArrayList<java_ManifestEntry> java_manifestentrys    ) {
        this.java_manifestattributes = java_manifestattributes;
        this.java_manifestentrys = java_manifestentrys;
    }


    public List<java_ManifestAttribute> getJava_manifestattributes() {
        return java_manifestattributes;
    }

    public void addJava_manifestattribute(Java_manifestattribute java_manifestattribute) {
        this.java_manifestattributes.add(java_manifestattribute);
    }
    public java_Archive getJava_archive() {
        return java_archive;
    }

    public void setJava_archive(java_Archive java_archive) {
        this.java_archive = java_archive;
    }
    public List<java_ManifestEntry> getJava_manifestentrys() {
        return java_manifestentrys;
    }

    public void addJava_manifestentry(Java_manifestentry java_manifestentry) {
        this.java_manifestentrys.add(java_manifestentry);
    }

}