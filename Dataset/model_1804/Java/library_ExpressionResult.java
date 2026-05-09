





import java.util.List;
import java.util.ArrayList;

public class library_ExpressionResult extends BaseExpressionResult {

    private String targetIntervalHint;
    private String targetKindHint;
    private String targetRange;





    private library_BaseResource library_baseresource;


    public library_ExpressionResult(
        String targetIntervalHint,        String targetKindHint,        String targetRange    ) {
        super(
        );
        this.targetIntervalHint = targetIntervalHint;
        this.targetKindHint = targetKindHint;
        this.targetRange = targetRange;
    }


    public String getTargetintervalhint() {
        return targetIntervalHint;
    }

    public void setTargetintervalhint(String targetIntervalHint) {
        this.targetIntervalHint = targetIntervalHint;
    }
    public String getTargetkindhint() {
        return targetKindHint;
    }

    public void setTargetkindhint(String targetKindHint) {
        this.targetKindHint = targetKindHint;
    }
    public String getTargetrange() {
        return targetRange;
    }

    public void setTargetrange(String targetRange) {
        this.targetRange = targetRange;
    }

    public library_BaseResource getLibrary_baseresource() {
        return library_baseresource;
    }

    public void setLibrary_baseresource(library_BaseResource library_baseresource) {
        this.library_baseresource = library_baseresource;
    }

}