





import java.util.List;
import java.util.ArrayList;

public class ImperativeOCL_CatchExp extends ImperativeExpression {






    private List<Type> types;


    public ImperativeOCL_CatchExp(
    ) {
        super(
        );
        this.types = new ArrayList<>();
    }

    public ImperativeOCL_CatchExp(
        ArrayList<Type> types    ) {
        this.types = types;
    }


    public List<Type> getTypes() {
        return types;
    }

    public void addType(Type type) {
        this.types.add(type);
    }

}