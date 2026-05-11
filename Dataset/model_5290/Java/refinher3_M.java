





import java.util.List;
import java.util.ArrayList;

public class refinher3_M  {

    private String id;





    private refinher3_DG refinher3_dg;




    private List<refinher3_E> refinher3_es;




    private List<refinher3_Foobar> refinher3_foobars;


    public refinher3_M(
        String id    ) {
        this.id = id;
        this.refinher3_es = new ArrayList<>();
        this.refinher3_foobars = new ArrayList<>();
    }

    public refinher3_M(
        String id        ArrayList<refinher3_E> refinher3_es,        ArrayList<refinher3_Foobar> refinher3_foobars    ) {
        this.id = id;
        this.refinher3_es = refinher3_es;
        this.refinher3_foobars = refinher3_foobars;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public refinher3_DG getRefinher3_dg() {
        return refinher3_dg;
    }

    public void setRefinher3_dg(refinher3_DG refinher3_dg) {
        this.refinher3_dg = refinher3_dg;
    }
    public List<refinher3_E> getRefinher3_es() {
        return refinher3_es;
    }

    public void addRefinher3_e(Refinher3_e refinher3_e) {
        this.refinher3_es.add(refinher3_e);
    }
    public List<refinher3_Foobar> getRefinher3_foobars() {
        return refinher3_foobars;
    }

    public void addRefinher3_foobar(Refinher3_foobar refinher3_foobar) {
        this.refinher3_foobars.add(refinher3_foobar);
    }

}