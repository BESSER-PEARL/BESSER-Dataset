





import java.util.List;
import java.util.ArrayList;

public class core_actionstep_OpenQuery extends ActionStep {

    private boolean readOnly;
    private String scrollMode;
    private boolean scrollable;
    private String holdabilityMode;
    private boolean useCache;



    public core_actionstep_OpenQuery(
        boolean readOnly,        String scrollMode,        boolean scrollable,        String holdabilityMode,        boolean useCache    ) {
        super(
        );
        this.readOnly = readOnly;
        this.scrollMode = scrollMode;
        this.scrollable = scrollable;
        this.holdabilityMode = holdabilityMode;
        this.useCache = useCache;
    }


    public boolean getReadonly() {
        return readOnly;
    }

    public void setReadonly(boolean readOnly) {
        this.readOnly = readOnly;
    }
    public String getScrollmode() {
        return scrollMode;
    }

    public void setScrollmode(String scrollMode) {
        this.scrollMode = scrollMode;
    }
    public boolean getScrollable() {
        return scrollable;
    }

    public void setScrollable(boolean scrollable) {
        this.scrollable = scrollable;
    }
    public String getHoldabilitymode() {
        return holdabilityMode;
    }

    public void setHoldabilitymode(String holdabilityMode) {
        this.holdabilityMode = holdabilityMode;
    }
    public boolean getUsecache() {
        return useCache;
    }

    public void setUsecache(boolean useCache) {
        this.useCache = useCache;
    }


}