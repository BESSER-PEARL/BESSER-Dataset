





import java.util.List;
import java.util.ArrayList;

public class XHTML_ColElement  {






    private List<Colgroup> colgroups;


    public XHTML_ColElement(
    ) {
        this.colgroups = new ArrayList<>();
    }

    public XHTML_ColElement(
        ArrayList<Colgroup> colgroups    ) {
        this.colgroups = colgroups;
    }


    public List<Colgroup> getColgroups() {
        return colgroups;
    }

    public void addColgroup(Colgroup colgroup) {
        this.colgroups.add(colgroup);
    }

}