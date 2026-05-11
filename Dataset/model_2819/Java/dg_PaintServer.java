





import java.util.List;
import java.util.ArrayList;

public class dg_PaintServer extends Definition {






    private List<dg_Transform> dg_transforms;


    public dg_PaintServer(
    ) {
        super(
        );
        this.dg_transforms = new ArrayList<>();
    }

    public dg_PaintServer(
        ArrayList<dg_Transform> dg_transforms    ) {
        this.dg_transforms = dg_transforms;
    }


    public List<dg_Transform> getDg_transforms() {
        return dg_transforms;
    }

    public void addDg_transform(Dg_transform dg_transform) {
        this.dg_transforms.add(dg_transform);
    }

}