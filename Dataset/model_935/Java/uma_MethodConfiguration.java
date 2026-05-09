





import java.util.List;
import java.util.ArrayList;

public class uma_MethodConfiguration extends MethodUnit {

    private String subtractedCategory;
    private String baseConfiguration;
    private String methodPackageSelection;
    private String defaultView;
    private String addedCategory;
    private String methodPluginSelection;
    private String processView;



    public uma_MethodConfiguration(
        String subtractedCategory,        String baseConfiguration,        String methodPackageSelection,        String defaultView,        String addedCategory,        String methodPluginSelection,        String processView    ) {
        super(
        );
        this.subtractedCategory = subtractedCategory;
        this.baseConfiguration = baseConfiguration;
        this.methodPackageSelection = methodPackageSelection;
        this.defaultView = defaultView;
        this.addedCategory = addedCategory;
        this.methodPluginSelection = methodPluginSelection;
        this.processView = processView;
    }


    public String getSubtractedcategory() {
        return subtractedCategory;
    }

    public void setSubtractedcategory(String subtractedCategory) {
        this.subtractedCategory = subtractedCategory;
    }
    public String getBaseconfiguration() {
        return baseConfiguration;
    }

    public void setBaseconfiguration(String baseConfiguration) {
        this.baseConfiguration = baseConfiguration;
    }
    public String getMethodpackageselection() {
        return methodPackageSelection;
    }

    public void setMethodpackageselection(String methodPackageSelection) {
        this.methodPackageSelection = methodPackageSelection;
    }
    public String getDefaultview() {
        return defaultView;
    }

    public void setDefaultview(String defaultView) {
        this.defaultView = defaultView;
    }
    public String getAddedcategory() {
        return addedCategory;
    }

    public void setAddedcategory(String addedCategory) {
        this.addedCategory = addedCategory;
    }
    public String getMethodpluginselection() {
        return methodPluginSelection;
    }

    public void setMethodpluginselection(String methodPluginSelection) {
        this.methodPluginSelection = methodPluginSelection;
    }
    public String getProcessview() {
        return processView;
    }

    public void setProcessview(String processView) {
        this.processView = processView;
    }


}