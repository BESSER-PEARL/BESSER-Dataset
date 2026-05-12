





import java.util.List;
import java.util.ArrayList;

public class rdal_InteractionVariable extends Variable {

    private boolean neglected;
    private String type;





    private rdal_SystemOverview rdal_systemoverview;




    private rdal_SystemContext rdal_systemcontext;


    public rdal_InteractionVariable(
        boolean neglected,        String type    ) {
        super(
        );
        this.neglected = neglected;
        this.type = type;
    }


    public boolean getNeglected() {
        return neglected;
    }

    public void setNeglected(boolean neglected) {
        this.neglected = neglected;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public rdal_SystemOverview getRdal_systemoverview() {
        return rdal_systemoverview;
    }

    public void setRdal_systemoverview(rdal_SystemOverview rdal_systemoverview) {
        this.rdal_systemoverview = rdal_systemoverview;
    }
    public rdal_SystemContext getRdal_systemcontext() {
        return rdal_systemcontext;
    }

    public void setRdal_systemcontext(rdal_SystemContext rdal_systemcontext) {
        this.rdal_systemcontext = rdal_systemcontext;
    }

}