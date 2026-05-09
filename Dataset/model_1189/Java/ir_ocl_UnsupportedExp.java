





import java.util.List;
import java.util.ArrayList;

public class ir_ocl_UnsupportedExp extends OclExpression {

    private String reason;
    private String description;



    public ir_ocl_UnsupportedExp(
        String reason,        String description    ) {
        super(
        );
        this.reason = reason;
        this.description = description;
    }


    public String getReason() {
        return reason;
    }

    public void setReason(String reason) {
        this.reason = reason;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}