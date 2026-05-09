





import java.util.List;
import java.util.ArrayList;

public class uma_MethodConfiguration extends MethodUnit {

    private String methodPackageSelection;
    private String baseConfiguration;
    private String addedCategory;
    private String methodPluginSelection;
    private String processView;
    private String defaultView;
    private String subtractedCategory;





    private uma_MethodLibrary uma_methodlibrary;


    public uma_MethodConfiguration(
        String methodPackageSelection,        String baseConfiguration,        String addedCategory,        String methodPluginSelection,        String processView,        String defaultView,        String subtractedCategory    ) {
        super(
        );
        this.methodPackageSelection = methodPackageSelection;
        this.baseConfiguration = baseConfiguration;
        this.addedCategory = addedCategory;
        this.methodPluginSelection = methodPluginSelection;
        this.processView = processView;
        this.defaultView = defaultView;
        this.subtractedCategory = subtractedCategory;
    }


    public String getMethodpackageselection() {
        return methodPackageSelection;
    }

    public void setMethodpackageselection(String methodPackageSelection) {
        this.methodPackageSelection = methodPackageSelection;
    }
    public String getBaseconfiguration() {
        return baseConfiguration;
    }

    public void setBaseconfiguration(String baseConfiguration) {
        this.baseConfiguration = baseConfiguration;
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
    public String getDefaultview() {
        return defaultView;
    }

    public void setDefaultview(String defaultView) {
        this.defaultView = defaultView;
    }
    public String getSubtractedcategory() {
        return subtractedCategory;
    }

    public void setSubtractedcategory(String subtractedCategory) {
        this.subtractedCategory = subtractedCategory;
    }

    public uma_MethodLibrary getUma_methodlibrary() {
        return uma_methodlibrary;
    }

    public void setUma_methodlibrary(uma_MethodLibrary uma_methodlibrary) {
        this.uma_methodlibrary = uma_methodlibrary;
    }

}