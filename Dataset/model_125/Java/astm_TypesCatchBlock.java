





import java.util.List;
import java.util.ArrayList;

public class astm_TypesCatchBlock extends CatchBlock {






    private List<Type> types;


    public astm_TypesCatchBlock(
    ) {
        super(
        );
        this.types = new ArrayList<>();
    }

    public astm_TypesCatchBlock(
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