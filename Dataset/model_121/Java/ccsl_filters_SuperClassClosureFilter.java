





import java.util.List;
import java.util.ArrayList;

public class ccsl_filters_SuperClassClosureFilter extends AtomicFilter {

    private String includesSubClass;





    private Context context;


    public ccsl_filters_SuperClassClosureFilter(
        String includesSubClass    ) {
        super(
        );
        this.includesSubClass = includesSubClass;
    }


    public String getIncludessubclass() {
        return includesSubClass;
    }

    public void setIncludessubclass(String includesSubClass) {
        this.includesSubClass = includesSubClass;
    }

    public Context getContext() {
        return context;
    }

    public void setContext(Context context) {
        this.context = context;
    }

}