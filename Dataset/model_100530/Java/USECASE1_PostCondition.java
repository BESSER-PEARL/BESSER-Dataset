





import java.util.List;
import java.util.ArrayList;

public class USECASE1_PostCondition  {






    private List<Context> contexts;


    public USECASE1_PostCondition(
    ) {
        this.contexts = new ArrayList<>();
    }

    public USECASE1_PostCondition(
        ArrayList<Context> contexts    ) {
        this.contexts = contexts;
    }


    public List<Context> getContexts() {
        return contexts;
    }

    public void addContext(Context context) {
        this.contexts.add(context);
    }

}