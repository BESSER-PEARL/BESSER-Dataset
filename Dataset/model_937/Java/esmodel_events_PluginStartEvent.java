





import java.util.List;
import java.util.ArrayList;

public class esmodel_events_PluginStartEvent extends Event {

    private String pluginId;



    public esmodel_events_PluginStartEvent(
        String pluginId    ) {
        super(
        );
        this.pluginId = pluginId;
    }


    public String getPluginid() {
        return pluginId;
    }

    public void setPluginid(String pluginId) {
        this.pluginId = pluginId;
    }


}