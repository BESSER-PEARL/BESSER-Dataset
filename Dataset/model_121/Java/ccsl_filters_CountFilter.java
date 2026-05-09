





import java.util.List;
import java.util.ArrayList;

public class ccsl_filters_CountFilter extends AtomicFilter {

    private String max;
    private String min;





    private List<Context> contexts;




    private Element element;




    private Element element;


    public ccsl_filters_CountFilter(
        String max,        String min    ) {
        super(
        );
        this.max = max;
        this.min = min;
        this.contexts = new ArrayList<>();
    }

    public ccsl_filters_CountFilter(
        String max,        String min        ArrayList<Context> contexts    ) {
        this.max = max;
        this.min = min;
        this.contexts = contexts;
    }

    public String getMax() {
        return max;
    }

    public void setMax(String max) {
        this.max = max;
    }
    public String getMin() {
        return min;
    }

    public void setMin(String min) {
        this.min = min;
    }

    public List<Context> getContexts() {
        return contexts;
    }

    public void addContext(Context context) {
        this.contexts.add(context);
    }
    public Element getElement() {
        return element;
    }

    public void setElement(Element element) {
        this.element = element;
    }
    public Element getElement() {
        return element;
    }

    public void setElement(Element element) {
        this.element = element;
    }

}