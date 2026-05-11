





import java.util.List;
import java.util.ArrayList;

public class smif_toplevel_Proposition extends IdentifiableEntity {






    private List<Context> contexts;




    private List<Context> contexts;


    public smif_toplevel_Proposition(
    ) {
        super(
        );
        this.contexts = new ArrayList<>();
        this.contexts = new ArrayList<>();
    }

    public smif_toplevel_Proposition(
        ArrayList<Context> contexts,        ArrayList<Context> contexts    ) {
        this.contexts = contexts;
        this.contexts = contexts;
    }


    public List<Context> getContexts() {
        return contexts;
    }

    public void addContext(Context context) {
        this.contexts.add(context);
    }
    public List<Context> getContexts() {
        return contexts;
    }

    public void addContext(Context context) {
        this.contexts.add(context);
    }

}