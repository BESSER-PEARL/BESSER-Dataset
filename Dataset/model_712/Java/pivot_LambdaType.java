





import java.util.List;
import java.util.ArrayList;

public class pivot_LambdaType extends DataType {






    private pivot_Type pivot_type;




    private pivot_Type pivot_type;




    private List<pivot_Type> pivot_types;


    public pivot_LambdaType(
    ) {
        super(
        );
        this.pivot_types = new ArrayList<>();
    }

    public pivot_LambdaType(
        ArrayList<pivot_Type> pivot_types    ) {
        this.pivot_types = pivot_types;
    }


    public pivot_Type getPivot_type() {
        return pivot_type;
    }

    public void setPivot_type(pivot_Type pivot_type) {
        this.pivot_type = pivot_type;
    }
    public pivot_Type getPivot_type() {
        return pivot_type;
    }

    public void setPivot_type(pivot_Type pivot_type) {
        this.pivot_type = pivot_type;
    }
    public List<pivot_Type> getPivot_types() {
        return pivot_types;
    }

    public void addPivot_type(Pivot_type pivot_type) {
        this.pivot_types.add(pivot_type);
    }

}