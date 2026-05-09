




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class esmodel_events_PluginFocusEvent extends Event {

    private LocalDate startDate;
    private String pluginId;



    public esmodel_events_PluginFocusEvent(
        LocalDate startDate,        String pluginId    ) {
        super(
        );
        this.startDate = startDate;
        this.pluginId = pluginId;
    }


    public LocalDate getStartdate() {
        return startDate;
    }

    public void setStartdate(LocalDate startDate) {
        this.startDate = startDate;
    }
    public String getPluginid() {
        return pluginId;
    }

    public void setPluginid(String pluginId) {
        this.pluginId = pluginId;
    }


}