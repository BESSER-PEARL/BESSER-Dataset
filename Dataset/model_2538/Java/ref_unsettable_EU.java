





import java.util.List;
import java.util.ArrayList;

public class ref_unsettable_EU  {

    private String labels;
    private String ids;
    private String name;





    private List<DU> dus;


    public ref_unsettable_EU(
        String labels,        String ids,        String name    ) {
        this.labels = labels;
        this.ids = ids;
        this.name = name;
        this.dus = new ArrayList<>();
    }

    public ref_unsettable_EU(
        String labels,        String ids,        String name        ArrayList<DU> dus    ) {
        this.labels = labels;
        this.ids = ids;
        this.name = name;
        this.dus = dus;
    }

    public String getLabels() {
        return labels;
    }

    public void setLabels(String labels) {
        this.labels = labels;
    }
    public String getIds() {
        return ids;
    }

    public void setIds(String ids) {
        this.ids = ids;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<DU> getDus() {
        return dus;
    }

    public void addDu(Du du) {
        this.dus.add(du);
    }

}