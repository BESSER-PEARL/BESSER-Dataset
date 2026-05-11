





import java.util.List;
import java.util.ArrayList;

public class smif_expressions_ExpressionContext extends IdentifiableEntity {






    private List<Type> types;




    private Context context;


    public smif_expressions_ExpressionContext(
    ) {
        super(
        );
        this.types = new ArrayList<>();
    }

    public smif_expressions_ExpressionContext(
        ArrayList<Type> types    ) {
        this.types = types;
    }


    public List<Type> getTypes() {
        return types;
    }

    public void addType(Type type) {
        this.types.add(type);
    }
    public Context getContext() {
        return context;
    }

    public void setContext(Context context) {
        this.context = context;
    }

}