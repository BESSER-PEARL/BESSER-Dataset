





import java.util.List;
import java.util.ArrayList;

public class YasperEPNML114_TransitionSpecific  {

    private String tool;
    private String tokenCaseSensitive;
    private String version;





    private YasperEPNML114_Cost yasperepnml114_cost;




    private YasperEPNML114_Roles yasperepnml114_roles;




    private YasperEPNML114_ProcessingTime yasperepnml114_processingtime;


    public YasperEPNML114_TransitionSpecific(
        String tool,        String tokenCaseSensitive,        String version    ) {
        this.tool = tool;
        this.tokenCaseSensitive = tokenCaseSensitive;
        this.version = version;
    }


    public String getTool() {
        return tool;
    }

    public void setTool(String tool) {
        this.tool = tool;
    }
    public String getTokencasesensitive() {
        return tokenCaseSensitive;
    }

    public void setTokencasesensitive(String tokenCaseSensitive) {
        this.tokenCaseSensitive = tokenCaseSensitive;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public YasperEPNML114_Cost getYasperepnml114_cost() {
        return yasperepnml114_cost;
    }

    public void setYasperepnml114_cost(YasperEPNML114_Cost yasperepnml114_cost) {
        this.yasperepnml114_cost = yasperepnml114_cost;
    }
    public YasperEPNML114_Roles getYasperepnml114_roles() {
        return yasperepnml114_roles;
    }

    public void setYasperepnml114_roles(YasperEPNML114_Roles yasperepnml114_roles) {
        this.yasperepnml114_roles = yasperepnml114_roles;
    }
    public YasperEPNML114_ProcessingTime getYasperepnml114_processingtime() {
        return yasperepnml114_processingtime;
    }

    public void setYasperepnml114_processingtime(YasperEPNML114_ProcessingTime yasperepnml114_processingtime) {
        this.yasperepnml114_processingtime = yasperepnml114_processingtime;
    }

}