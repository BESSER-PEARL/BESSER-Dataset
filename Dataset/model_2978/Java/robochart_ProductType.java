





import java.util.List;
import java.util.ArrayList;

public class robochart_ProductType extends Type {






    private List<robochart_Type> robochart_types;


    public robochart_ProductType(
    ) {
        super(
        );
        this.robochart_types = new ArrayList<>();
    }

    public robochart_ProductType(
        ArrayList<robochart_Type> robochart_types    ) {
        this.robochart_types = robochart_types;
    }


    public List<robochart_Type> getRobochart_types() {
        return robochart_types;
    }

    public void addRobochart_type(Robochart_type robochart_type) {
        this.robochart_types.add(robochart_type);
    }

}