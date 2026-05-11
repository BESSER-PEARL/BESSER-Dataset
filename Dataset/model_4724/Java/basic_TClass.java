





import java.util.List;
import java.util.ArrayList;

public class basic_TClass extends TAbstractType {






    private basic_TypeGraph basic_typegraph;




    private basic_TPackage basic_tpackage;




    private basic_TClass basic_tclass;




    private List<basic_TClass> basic_tclasss;


    public basic_TClass(
    ) {
        super(
        );
        this.basic_tclasss = new ArrayList<>();
    }

    public basic_TClass(
        ArrayList<basic_TClass> basic_tclasss    ) {
        this.basic_tclasss = basic_tclasss;
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
    public basic_TClass getBasic_tclass() {
        return basic_tclass;
    }

    public void setBasic_tclass(basic_TClass basic_tclass) {
        this.basic_tclass = basic_tclass;
    }
    public List<basic_TClass> getBasic_tclasss() {
        return basic_tclasss;
    }

    public void addBasic_tclass(Basic_tclass basic_tclass) {
        this.basic_tclasss.add(basic_tclass);
    }

}