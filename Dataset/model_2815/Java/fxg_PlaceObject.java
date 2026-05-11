





import java.util.List;
import java.util.ArrayList;

public class fxg_PlaceObject extends FXGElement {

    private String id;





    private fxg_Transform fxg_transform;




    private List<fxg_Filter> fxg_filters;




    private fxg_Group fxg_group;


    public fxg_PlaceObject(
        String id    ) {
        super(
        );
        this.id = id;
        this.fxg_filters = new ArrayList<>();
    }

    public fxg_PlaceObject(
        String id        ArrayList<fxg_Filter> fxg_filters    ) {
        this.id = id;
        this.fxg_filters = fxg_filters;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public fxg_Transform getFxg_transform() {
        return fxg_transform;
    }

    public void setFxg_transform(fxg_Transform fxg_transform) {
        this.fxg_transform = fxg_transform;
    }
    public List<fxg_Filter> getFxg_filters() {
        return fxg_filters;
    }

    public void addFxg_filter(Fxg_filter fxg_filter) {
        this.fxg_filters.add(fxg_filter);
    }
    public fxg_Group getFxg_group() {
        return fxg_group;
    }

    public void setFxg_group(fxg_Group fxg_group) {
        this.fxg_group = fxg_group;
    }

}