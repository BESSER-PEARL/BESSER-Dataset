





import java.util.List;
import java.util.ArrayList;

public class fxg_PlaceObject extends FXGElement {

    private String id;





    private fxg_Group fxg_group;




    private fxg_Transform fxg_transform;


    public fxg_PlaceObject(
        String id    ) {
        super(
        );
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public fxg_Group getFxg_group() {
        return fxg_group;
    }

    public void setFxg_group(fxg_Group fxg_group) {
        this.fxg_group = fxg_group;
    }
    public fxg_Transform getFxg_transform() {
        return fxg_transform;
    }

    public void setFxg_transform(fxg_Transform fxg_transform) {
        this.fxg_transform = fxg_transform;
    }

}