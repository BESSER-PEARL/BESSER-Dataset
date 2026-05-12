





import java.util.List;
import java.util.ArrayList;

public class pivot_Operation extends Feature, Namespace, TemplateableElement {

    private String isValidating;
    private String isTypeof;
    private String isInvalidating;





    private List<pivot_Operation> pivot_operations;


    public pivot_Operation(
        String isValidating,        String isTypeof,        String isInvalidating    ) {
        super(
        );
        this.isValidating = isValidating;
        this.isTypeof = isTypeof;
        this.isInvalidating = isInvalidating;
        this.pivot_operations = new ArrayList<>();
    }

    public pivot_Operation(
        String isValidating,        String isTypeof,        String isInvalidating        ArrayList<pivot_Operation> pivot_operations    ) {
        this.isValidating = isValidating;
        this.isTypeof = isTypeof;
        this.isInvalidating = isInvalidating;
        this.pivot_operations = pivot_operations;
    }

    public String getIsvalidating() {
        return isValidating;
    }

    public void setIsvalidating(String isValidating) {
        this.isValidating = isValidating;
    }
    public String getIstypeof() {
        return isTypeof;
    }

    public void setIstypeof(String isTypeof) {
        this.isTypeof = isTypeof;
    }
    public String getIsinvalidating() {
        return isInvalidating;
    }

    public void setIsinvalidating(String isInvalidating) {
        this.isInvalidating = isInvalidating;
    }

    public List<pivot_Operation> getPivot_operations() {
        return pivot_operations;
    }

    public void addPivot_operation(Pivot_operation pivot_operation) {
        this.pivot_operations.add(pivot_operation);
    }

}