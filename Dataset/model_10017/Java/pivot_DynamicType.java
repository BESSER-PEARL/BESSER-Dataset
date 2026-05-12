





import java.util.List;
import java.util.ArrayList;

public class pivot_DynamicType extends DynamicElement, Class {






    private List<pivot_DynamicProperty> pivot_dynamicpropertys;


    public pivot_DynamicType(
    ) {
        super(
        );
        this.pivot_dynamicpropertys = new ArrayList<>();
    }

    public pivot_DynamicType(
        ArrayList<pivot_DynamicProperty> pivot_dynamicpropertys    ) {
        this.pivot_dynamicpropertys = pivot_dynamicpropertys;
    }


    public List<pivot_DynamicProperty> getPivot_dynamicpropertys() {
        return pivot_dynamicpropertys;
    }

    public void addPivot_dynamicproperty(Pivot_dynamicproperty pivot_dynamicproperty) {
        this.pivot_dynamicpropertys.add(pivot_dynamicproperty);
    }

}