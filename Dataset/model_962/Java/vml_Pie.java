





import java.util.List;
import java.util.ArrayList;

public class vml_Pie  {

    private String ID;
    private String title;





    private vml_Diagram vml_diagram;




    private List<vml_Slice> vml_slices;


    public vml_Pie(
        String ID,        String title    ) {
        this.ID = ID;
        this.title = title;
        this.vml_slices = new ArrayList<>();
    }

    public vml_Pie(
        String ID,        String title        ArrayList<vml_Slice> vml_slices    ) {
        this.ID = ID;
        this.title = title;
        this.vml_slices = vml_slices;
    }

    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public vml_Diagram getVml_diagram() {
        return vml_diagram;
    }

    public void setVml_diagram(vml_Diagram vml_diagram) {
        this.vml_diagram = vml_diagram;
    }
    public List<vml_Slice> getVml_slices() {
        return vml_slices;
    }

    public void addVml_slice(Vml_slice vml_slice) {
        this.vml_slices.add(vml_slice);
    }

}