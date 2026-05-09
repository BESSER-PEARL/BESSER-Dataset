





import java.util.List;
import java.util.ArrayList;

public class pivot_AssociationClass extends Class {






    private List<pivot_Property> pivot_propertys;




    private pivot_Property pivot_property;


    public pivot_AssociationClass(
    ) {
        super(
        );
        this.pivot_propertys = new ArrayList<>();
    }

    public pivot_AssociationClass(
        ArrayList<pivot_Property> pivot_propertys    ) {
        this.pivot_propertys = pivot_propertys;
    }


    public List<pivot_Property> getPivot_propertys() {
        return pivot_propertys;
    }

    public void addPivot_property(Pivot_property pivot_property) {
        this.pivot_propertys.add(pivot_property);
    }
    public pivot_Property getPivot_property() {
        return pivot_property;
    }

    public void setPivot_property(pivot_Property pivot_property) {
        this.pivot_property = pivot_property;
    }

}