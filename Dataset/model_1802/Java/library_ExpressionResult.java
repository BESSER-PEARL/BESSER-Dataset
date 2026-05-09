





import java.util.List;
import java.util.ArrayList;

public class library_ExpressionResult extends BaseExpressionResult {

    private String targetIntervalHint;
    private String targetRange;
    private String targetKindHint;





    private List<library_Value> library_values;




    private library_BaseResource library_baseresource;


    public library_ExpressionResult(
        String targetIntervalHint,        String targetRange,        String targetKindHint    ) {
        super(
        );
        this.targetIntervalHint = targetIntervalHint;
        this.targetRange = targetRange;
        this.targetKindHint = targetKindHint;
        this.library_values = new ArrayList<>();
    }

    public library_ExpressionResult(
        String targetIntervalHint,        String targetRange,        String targetKindHint        ArrayList<library_Value> library_values    ) {
        this.targetIntervalHint = targetIntervalHint;
        this.targetRange = targetRange;
        this.targetKindHint = targetKindHint;
        this.library_values = library_values;
    }

    public String getTargetintervalhint() {
        return targetIntervalHint;
    }

    public void setTargetintervalhint(String targetIntervalHint) {
        this.targetIntervalHint = targetIntervalHint;
    }
    public String getTargetrange() {
        return targetRange;
    }

    public void setTargetrange(String targetRange) {
        this.targetRange = targetRange;
    }
    public String getTargetkindhint() {
        return targetKindHint;
    }

    public void setTargetkindhint(String targetKindHint) {
        this.targetKindHint = targetKindHint;
    }

    public List<library_Value> getLibrary_values() {
        return library_values;
    }

    public void addLibrary_value(Library_value library_value) {
        this.library_values.add(library_value);
    }
    public library_BaseResource getLibrary_baseresource() {
        return library_baseresource;
    }

    public void setLibrary_baseresource(library_BaseResource library_baseresource) {
        this.library_baseresource = library_baseresource;
    }

}