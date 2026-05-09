





import java.util.List;
import java.util.ArrayList;

public class library_ExpressionResult extends BaseExpressionResult {

    private String targetRange;
    private String targetKindHint;
    private String targetIntervalHint;





    private library_BaseResource library_baseresource;


    public library_ExpressionResult(
        String targetRange,        String targetKindHint,        String targetIntervalHint    ) {
        super(
        );
        this.targetRange = targetRange;
        this.targetKindHint = targetKindHint;
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
    public String getTargetintervalhint() {
        return targetIntervalHint;
    }

    public void setTargetintervalhint(String targetIntervalHint) {
        this.targetIntervalHint = targetIntervalHint;
    }

    public library_BaseResource getLibrary_baseresource() {
        return library_baseresource;
    }

    public void setLibrary_baseresource(library_BaseResource library_baseresource) {
        this.library_baseresource = library_baseresource;
    }

}