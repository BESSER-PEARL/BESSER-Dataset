





import java.util.List;
import java.util.ArrayList;

public class model_NotificationDefinition extends BasicNotificationDefinition {

    private boolean template;
    private String excludeFilter;
    private String includeFilter;



    public model_NotificationDefinition(
        boolean template,        String excludeFilter,        String includeFilter    ) {
        super(
        );
        this.template = template;
        this.excludeFilter = excludeFilter;
        this.includeFilter = includeFilter;
    }


    public boolean getTemplate() {
        return template;
    }

    public void setTemplate(boolean template) {
        this.template = template;
    }
    public String getExcludefilter() {
        return excludeFilter;
    }

    public void setExcludefilter(String excludeFilter) {
        this.excludeFilter = excludeFilter;
    }
    public String getIncludefilter() {
        return includeFilter;
    }

    public void setIncludefilter(String includeFilter) {
        this.includeFilter = includeFilter;
    }


}