





import java.util.List;
import java.util.ArrayList;

public class d_D  {

    private String name;
    private String atts;





    private List<d_D> d_ds;


    public d_D(
        String name,        String atts    ) {
        this.name = name;
        this.atts = atts;
        this.d_ds = new ArrayList<>();
    }

    public d_D(
        String name,        String atts        ArrayList<d_D> d_ds    ) {
        this.name = name;
        this.atts = atts;
        this.d_ds = d_ds;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAtts() {
        return atts;
    }

    public void setAtts(String atts) {
        this.atts = atts;
    }

    public List<d_D> getD_ds() {
        return d_ds;
    }

    public void addD_d(D_d d_d) {
        this.d_ds.add(d_d);
    }

}