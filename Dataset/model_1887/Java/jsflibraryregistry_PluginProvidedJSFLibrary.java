





import java.util.List;
import java.util.ArrayList;

public class jsflibraryregistry_PluginProvidedJSFLibrary extends JSFLibrary {

    private String pluginID;
    private String Label;





    private jsflibraryregistry_JSFLibraryRegistry jsflibraryregistry_jsflibraryregistry;


    public jsflibraryregistry_PluginProvidedJSFLibrary(
        String pluginID,        String Label    ) {
        super(
        );
        this.pluginID = pluginID;
        this.Label = Label;
    }


    public String getPluginid() {
        return pluginID;
    }

    public void setPluginid(String pluginID) {
        this.pluginID = pluginID;
    }
    public String getLabel() {
        return Label;
    }

    public void setLabel(String Label) {
        this.Label = Label;
    }

    public jsflibraryregistry_JSFLibraryRegistry getJsflibraryregistry_jsflibraryregistry() {
        return jsflibraryregistry_jsflibraryregistry;
    }

    public void setJsflibraryregistry_jsflibraryregistry(jsflibraryregistry_JSFLibraryRegistry jsflibraryregistry_jsflibraryregistry) {
        this.jsflibraryregistry_jsflibraryregistry = jsflibraryregistry_jsflibraryregistry;
    }

}