





import java.util.List;
import java.util.ArrayList;

public class uma_MethodConfiguration extends MethodUnit {

    private String methodPluginSelection;
    private String subtractedCategory;
    private String processView;
    private String addedCategory;
    private String baseConfiguration;
    private String methodPackageSelection;
    private String defaultView;





    private uma_MethodLibrary uma_methodlibrary;


    public uma_MethodConfiguration(
        String methodPluginSelection,        String subtractedCategory,        String processView,        String addedCategory,        String baseConfiguration,        String methodPackageSelection,        String defaultView    ) {
        super(
        );
        this.methodPluginSelection = methodPluginSelection;
        this.subtractedCategory = subtractedCategory;
        this.processView = processView;
        this.addedCategory = addedCategory;
        this.baseConfiguration = baseConfiguration;
        this.methodPackageSelection = methodPackageSelection;
        this.defaultView = defaultView;
    }


    public String getMethodpluginselection() {
        return methodPluginSelection;
    }

    public void setMethodpluginselection(String methodPluginSelection) {
        this.methodPluginSelection = methodPluginSelection;
    }
    public String getSubtractedcategory() {
        return subtractedCategory;
    }

    public void setSubtractedcategory(String subtractedCategory) {
        this.subtractedCategory = subtractedCategory;
    }
    public String getProcessview() {
        return processView;
    }

    public void setProcessview(String processView) {
        this.processView = processView;
    }
    public String getAddedcategory() {
        return addedCategory;
    }

    public void setAddedcategory(String addedCategory) {
        this.addedCategory = addedCategory;
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

    public uma_MethodLibrary getUma_methodlibrary() {
        return uma_methodlibrary;
    }

    public void setUma_methodlibrary(uma_MethodLibrary uma_methodlibrary) {
        this.uma_methodlibrary = uma_methodlibrary;
    }

}