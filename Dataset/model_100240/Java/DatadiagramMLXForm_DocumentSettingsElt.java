





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLXForm_DocumentSettingsElt  {

    private String glueSettings;
    private String protectShapes;
    private String customToolbarsFile;
    private String snapSettings;
    private String snapExtensions;
    private String protectStyles;
    private String protectMasters;
    private String dynamicGridEnabled;
    private String customMenusFile;
    private String protectBkgnds;
    private String attachedToolbars;





    private VisioDocument visiodocument;


    public DatadiagramMLXForm_DocumentSettingsElt(
        String glueSettings,        String protectShapes,        String customToolbarsFile,        String snapSettings,        String snapExtensions,        String protectStyles,        String protectMasters,        String dynamicGridEnabled,        String customMenusFile,        String protectBkgnds,        String attachedToolbars    ) {
        this.glueSettings = glueSettings;
        this.protectShapes = protectShapes;
        this.customToolbarsFile = customToolbarsFile;
        this.snapSettings = snapSettings;
        this.snapExtensions = snapExtensions;
        this.protectStyles = protectStyles;
        this.protectMasters = protectMasters;
        this.dynamicGridEnabled = dynamicGridEnabled;
        this.customMenusFile = customMenusFile;
        this.protectBkgnds = protectBkgnds;
        this.attachedToolbars = attachedToolbars;
    }


    public String getGluesettings() {
        return glueSettings;
    }

    public void setGluesettings(String glueSettings) {
        this.glueSettings = glueSettings;
    }
    public String getProtectshapes() {
        return protectShapes;
    }

    public void setProtectshapes(String protectShapes) {
        this.protectShapes = protectShapes;
    }
    public String getCustomtoolbarsfile() {
        return customToolbarsFile;
    }

    public void setCustomtoolbarsfile(String customToolbarsFile) {
        this.customToolbarsFile = customToolbarsFile;
    }
    public String getSnapsettings() {
        return snapSettings;
    }

    public void setSnapsettings(String snapSettings) {
        this.snapSettings = snapSettings;
    }
    public String getSnapextensions() {
        return snapExtensions;
    }

    public void setSnapextensions(String snapExtensions) {
        this.snapExtensions = snapExtensions;
    }
    public String getProtectstyles() {
        return protectStyles;
    }

    public void setProtectstyles(String protectStyles) {
        this.protectStyles = protectStyles;
    }
    public String getProtectmasters() {
        return protectMasters;
    }

    public void setProtectmasters(String protectMasters) {
        this.protectMasters = protectMasters;
    }
    public String getDynamicgridenabled() {
        return dynamicGridEnabled;
    }

    public void setDynamicgridenabled(String dynamicGridEnabled) {
        this.dynamicGridEnabled = dynamicGridEnabled;
    }
    public String getCustommenusfile() {
        return customMenusFile;
    }

    public void setCustommenusfile(String customMenusFile) {
        this.customMenusFile = customMenusFile;
    }
    public String getProtectbkgnds() {
        return protectBkgnds;
    }

    public void setProtectbkgnds(String protectBkgnds) {
        this.protectBkgnds = protectBkgnds;
    }
    public String getAttachedtoolbars() {
        return attachedToolbars;
    }

    public void setAttachedtoolbars(String attachedToolbars) {
        this.attachedToolbars = attachedToolbars;
    }

    public VisioDocument getVisiodocument() {
        return visiodocument;
    }

    public void setVisiodocument(VisioDocument visiodocument) {
        this.visiodocument = visiodocument;
    }

}