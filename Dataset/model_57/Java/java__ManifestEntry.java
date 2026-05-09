





import java.util.List;
import java.util.ArrayList;

public class java__ManifestEntry  {

    private String name;





    private List<java__ManifestAttribute> java__manifestattributes;


    public java__ManifestEntry(
        String name    ) {
        this.name = name;
        this.java__manifestattributes = new ArrayList<>();
    }

    public java__ManifestEntry(
        String name        ArrayList<java__ManifestAttribute> java__manifestattributes    ) {
        this.name = name;
        this.java__manifestattributes = java__manifestattributes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<java__ManifestAttribute> getJava__manifestattributes() {
        return java__manifestattributes;
    }

    public void addJava__manifestattribute(Java__manifestattribute java__manifestattribute) {
        this.java__manifestattributes.add(java__manifestattribute);
    }

}