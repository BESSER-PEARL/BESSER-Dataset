




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class esmodel_events_PluginFocusEvent extends Event {

    private String pluginId;
    private LocalDate startDate;



    public esmodel_events_PluginFocusEvent(
        String pluginId,        LocalDate startDate    ) {
        super(
        );
        this.pluginId = pluginId;
        this.startDate = startDate;
    }


    public String getPluginid() {
        return pluginId;
    }

    public void setPluginid(String pluginId) {
        this.pluginId = pluginId;
    }
    public LocalDate getStartdate() {
        return startDate;
    }

    public void setStartdate(LocalDate startDate) {
        this.startDate = startDate;
    }


}