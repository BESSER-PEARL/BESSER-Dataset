





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_schema_Event extends SQLObject {

    private String for_;
    private boolean enabled;
    private String action;
    private String condition;



    public sqlmodel_schema_Event(
        String for_,        boolean enabled,        String action,        String condition    ) {
        super(
        );
        this.for_ = for_;
        this.enabled = enabled;
        this.action = action;
        this.condition = condition;
    }


    public String getFor_() {
        return for_;
    }

    public void setFor_(String for_) {
        this.for_ = for_;
    }
    public boolean getEnabled() {
        return enabled;
    }

    public void setEnabled(boolean enabled) {
        this.enabled = enabled;
    }
    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }
    public String getCondition() {
        return condition;
    }

    public void setCondition(String condition) {
        this.condition = condition;
    }


}