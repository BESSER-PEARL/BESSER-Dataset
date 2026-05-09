





import java.util.List;
import java.util.ArrayList;

public class basic_Library  {

    private String versions;
    private String name;
    private boolean builtin;
    private String senchaTouchVersions;





    private List<basic_LibrarySource> basic_librarysources;


    public basic_Library(
        String versions,        String name,        boolean builtin,        String senchaTouchVersions    ) {
        this.versions = versions;
        this.name = name;
        this.builtin = builtin;
        this.senchaTouchVersions = senchaTouchVersions;
        this.basic_librarysources = new ArrayList<>();
    }

    public basic_Library(
        String versions,        String name,        boolean builtin,        String senchaTouchVersions        ArrayList<basic_LibrarySource> basic_librarysources    ) {
        this.versions = versions;
        this.name = name;
        this.builtin = builtin;
        this.senchaTouchVersions = senchaTouchVersions;
        this.basic_librarysources = basic_librarysources;
    }

    public String getVersions() {
        return versions;
    }

    public void setVersions(String versions) {
        this.versions = versions;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getBuiltin() {
        return builtin;
    }

    public void setBuiltin(boolean builtin) {
        this.builtin = builtin;
    }
    public String getSenchatouchversions() {
        return senchaTouchVersions;
    }

    public void setSenchatouchversions(String senchaTouchVersions) {
        this.senchaTouchVersions = senchaTouchVersions;
    }

    public List<basic_LibrarySource> getBasic_librarysources() {
        return basic_librarysources;
    }

    public void addBasic_librarysource(Basic_librarysource basic_librarysource) {
        this.basic_librarysources.add(basic_librarysource);
    }

}