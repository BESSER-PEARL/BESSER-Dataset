





import java.util.List;
import java.util.ArrayList;

public class uma_MethodConfiguration extends MethodUnit {

    private String addedCategory;
    private String methodPackageSelection;
    private String processView;
    private String subtractedCategory;
    private String methodPluginSelection;
    private String baseConfiguration;
    private String defaultView;



    public uma_MethodConfiguration(
        String addedCategory,        String methodPackageSelection,        String processView,        String subtractedCategory,        String methodPluginSelection,        String baseConfiguration,        String defaultView    ) {
        super(
        );
        this.addedCategory = addedCategory;
        this.methodPackageSelection = methodPackageSelection;
        this.processView = processView;
        this.subtractedCategory = subtractedCategory;
        this.methodPluginSelection = methodPluginSelection;
        this.baseConfiguration = baseConfiguration;
        this.defaultView = defaultView;
    }


    public String getAddedcategory() {
        return addedCategory;
    }

    public void setAddedcategory(String addedCategory) {
        this.addedCategory = addedCategory;
    }
    public String getMethodpackageselection() {
        return methodPackageSelection;
    }

    public void setMethodpackageselection(String methodPackageSelection) {
        this.methodPackageSelection = methodPackageSelection;
    }
    public String getProcessview() {
        return processView;
    }

    public void setProcessview(String processView) {
        this.processView = processView;
    }
    public String getSubtractedcategory() {
        return subtractedCategory;
    }

    public void setSubtractedcategory(String subtractedCategory) {
        this.subtractedCategory = subtractedCategory;
    }
    public String getMethodpluginselection() {
        return methodPluginSelection;
    }

    public void setMethodpluginselection(String methodPluginSelection) {
        this.methodPluginSelection = methodPluginSelection;
    }
    public String getBaseconfiguration() {
        return baseConfiguration;
    }

    public void setBaseconfiguration(String baseConfiguration) {
        this.baseConfiguration = baseConfiguration;
    }
    public String getDefaultview() {
        return defaultView;
    }

    public void setDefaultview(String defaultView) {
        this.defaultView = defaultView;
    }


}