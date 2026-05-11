





import java.util.List;
import java.util.ArrayList;

public class basic_TPackage extends TAnnotatable, TElementWithId {

    private String tName;





    private basic_TypeGraph basic_typegraph;




    private basic_TPackage basic_tpackage;




    private basic_TypeGraph basic_typegraph;




    private List<basic_TPackage> basic_tpackages;




    private basic_TypeGraph basic_typegraph;


    public basic_TPackage(
        String tName    ) {
        super(
        );
        this.tName = tName;
        this.basic_tpackages = new ArrayList<>();
    }

    public basic_TPackage(
        String tName        ArrayList<basic_TPackage> basic_tpackages    ) {
        this.tName = tName;
        this.basic_tpackages = basic_tpackages;
    }

    public String getTname() {
        return tName;
    }

    public void setTname(String tName) {
        this.tName = tName;
    }

    public basic_TypeGraph getBasic_typegraph() {
        return basic_typegraph;
    }

    public void setBasic_typegraph(basic_TypeGraph basic_typegraph) {
        this.basic_typegraph = basic_typegraph;
    }
    public basic_TPackage getBasic_tpackage() {
        return basic_tpackage;
    }

    public void setBasic_tpackage(basic_TPackage basic_tpackage) {
        this.basic_tpackage = basic_tpackage;
    }
    public basic_TypeGraph getBasic_typegraph() {
        return basic_typegraph;
    }

    public void setBasic_typegraph(basic_TypeGraph basic_typegraph) {
        this.basic_typegraph = basic_typegraph;
    }
    public List<basic_TPackage> getBasic_tpackages() {
        return basic_tpackages;
    }

    public void addBasic_tpackage(Basic_tpackage basic_tpackage) {
        this.basic_tpackages.add(basic_tpackage);
    }
    public basic_TypeGraph getBasic_typegraph() {
        return basic_typegraph;
    }

    public void setBasic_typegraph(basic_TypeGraph basic_typegraph) {
        this.basic_typegraph = basic_typegraph;
    }

}