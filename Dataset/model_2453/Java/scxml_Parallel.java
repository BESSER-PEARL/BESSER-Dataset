





import java.util.List;
import java.util.ArrayList;

public class scxml_Parallel extends NamedElement {

    private String id;





    private List<scxml_Parallel> scxml_parallels;


    public scxml_Parallel(
        String id    ) {
        super(
        );
        this.id = id;
        this.scxml_parallels = new ArrayList<>();
    }

    public scxml_Parallel(
        String id        ArrayList<scxml_Parallel> scxml_parallels    ) {
        this.id = id;
        this.scxml_parallels = scxml_parallels;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<scxml_Parallel> getScxml_parallels() {
        return scxml_parallels;
    }

    public void addScxml_parallel(Scxml_parallel scxml_parallel) {
        this.scxml_parallels.add(scxml_parallel);
    }

}