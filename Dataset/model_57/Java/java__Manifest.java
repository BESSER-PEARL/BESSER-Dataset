





import java.util.List;
import java.util.ArrayList;

public class java__Manifest  {






    private List<java__ManifestAttribute> java__manifestattributes;




    private java__Archive java__archive;




    private List<java__ManifestEntry> java__manifestentrys;


    public java__Manifest(
    ) {
        this.java__manifestattributes = new ArrayList<>();
        this.java__manifestentrys = new ArrayList<>();
    }

    public java__Manifest(
        ArrayList<java__ManifestAttribute> java__manifestattributes,        ArrayList<java__ManifestEntry> java__manifestentrys    ) {
        this.java__manifestattributes = java__manifestattributes;
        this.java__manifestentrys = java__manifestentrys;
    }


    public List<java__ManifestAttribute> getJava__manifestattributes() {
        return java__manifestattributes;
    }

    public void addJava__manifestattribute(Java__manifestattribute java__manifestattribute) {
        this.java__manifestattributes.add(java__manifestattribute);
    }
    public java__Archive getJava__archive() {
        return java__archive;
    }

    public void setJava__archive(java__Archive java__archive) {
        this.java__archive = java__archive;
    }
    public List<java__ManifestEntry> getJava__manifestentrys() {
        return java__manifestentrys;
    }

    public void addJava__manifestentry(Java__manifestentry java__manifestentry) {
        this.java__manifestentrys.add(java__manifestentry);
    }

}