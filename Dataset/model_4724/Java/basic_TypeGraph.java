





import java.util.List;
import java.util.ArrayList;

public class basic_TypeGraph extends TElementWithId {

    private String tName;





    private List<basic_TField> basic_tfields;




    private basic_TField basic_tfield;


    public basic_TypeGraph(
        String tName    ) {
        super(
        );
        this.tName = tName;
        this.basic_tfields = new ArrayList<>();
    }

    public basic_TypeGraph(
        String tName        ArrayList<basic_TField> basic_tfields    ) {
        this.tName = tName;
        this.basic_tfields = basic_tfields;
    }

    public String getTname() {
        return tName;
    }

    public void setTname(String tName) {
        this.tName = tName;
    }

    public List<basic_TField> getBasic_tfields() {
        return basic_tfields;
    }

    public void addBasic_tfield(Basic_tfield basic_tfield) {
        this.basic_tfields.add(basic_tfield);
    }
    public basic_TField getBasic_tfield() {
        return basic_tfield;
    }

    public void setBasic_tfield(basic_TField basic_tfield) {
        this.basic_tfield = basic_tfield;
    }

}