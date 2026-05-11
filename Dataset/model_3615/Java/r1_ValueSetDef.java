





import java.util.List;
import java.util.ArrayList;

public class r1_ValueSetDef extends Element {

    private String version;
    private String id;
    private String name;
    private String accessLevel;





    private List<r1_CodeSystemRef> r1_codesystemrefs;


    public r1_ValueSetDef(
        String version,        String id,        String name,        String accessLevel    ) {
        super(
        );
        this.version = version;
        this.id = id;
        this.name = name;
        this.accessLevel = accessLevel;
        this.r1_codesystemrefs = new ArrayList<>();
    }

    public r1_ValueSetDef(
        String version,        String id,        String name,        String accessLevel        ArrayList<r1_CodeSystemRef> r1_codesystemrefs    ) {
        this.version = version;
        this.id = id;
        this.name = name;
        this.accessLevel = accessLevel;
        this.r1_codesystemrefs = r1_codesystemrefs;
    }

    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAccesslevel() {
        return accessLevel;
    }

    public void setAccesslevel(String accessLevel) {
        this.accessLevel = accessLevel;
    }

    public List<r1_CodeSystemRef> getR1_codesystemrefs() {
        return r1_codesystemrefs;
    }

    public void addR1_codesystemref(R1_codesystemref r1_codesystemref) {
        this.r1_codesystemrefs.add(r1_codesystemref);
    }

}