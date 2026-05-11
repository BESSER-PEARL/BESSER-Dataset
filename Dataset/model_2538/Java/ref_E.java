





import java.util.List;
import java.util.ArrayList;

public class ref_E  {

    private String labels;
    private String name;
    private String ids;





    private List<ref_D> ref_ds;




    private ref_D ref_d;


    public ref_E(
        String labels,        String name,        String ids    ) {
        this.labels = labels;
        this.name = name;
        this.ids = ids;
        this.ref_ds = new ArrayList<>();
    }

    public ref_E(
        String labels,        String name,        String ids        ArrayList<ref_D> ref_ds    ) {
        this.labels = labels;
        this.name = name;
        this.ids = ids;
        this.ref_ds = ref_ds;
    }

    public String getLabels() {
        return labels;
    }

    public void setLabels(String labels) {
        this.labels = labels;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getIds() {
        return ids;
    }

    public void setIds(String ids) {
        this.ids = ids;
    }

    public List<ref_D> getRef_ds() {
        return ref_ds;
    }

    public void addRef_d(Ref_d ref_d) {
        this.ref_ds.add(ref_d);
    }
    public ref_D getRef_d() {
        return ref_d;
    }

    public void setRef_d(ref_D ref_d) {
        this.ref_d = ref_d;
    }

}