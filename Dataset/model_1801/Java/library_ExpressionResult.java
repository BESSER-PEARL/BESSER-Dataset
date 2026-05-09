





import java.util.List;
import java.util.ArrayList;

public class library_ExpressionResult extends BaseExpressionResult {

    private String targetRange;
    private String targetIntervalHint;
    private String targetKindHint;



    public library_ExpressionResult(
        String targetRange,        String targetIntervalHint,        String targetKindHint    ) {
        super(
        );
        this.targetRange = targetRange;
        this.targetIntervalHint = targetIntervalHint;
        this.targetKindHint = targetKindHint;
    }


    public String getTargetrange() {
        return targetRange;
    }

    public void setTargetrange(String targetRange) {
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


}