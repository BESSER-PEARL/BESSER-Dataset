





import java.util.List;
import java.util.ArrayList;

public class internalsm_State  {

    private String label;





    private internalsm_EventToken internalsm_eventtoken;




    private List<internalsm_EventToken> internalsm_eventtokens;


    public internalsm_State(
        String label    ) {
        this.label = label;
        this.internalsm_eventtokens = new ArrayList<>();
    }

    public internalsm_State(
        String label        ArrayList<internalsm_EventToken> internalsm_eventtokens    ) {
        this.label = label;
        this.internalsm_eventtokens = internalsm_eventtokens;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public internalsm_EventToken getInternalsm_eventtoken() {
        return internalsm_eventtoken;
    }

    public void setInternalsm_eventtoken(internalsm_EventToken internalsm_eventtoken) {
        this.internalsm_eventtoken = internalsm_eventtoken;
    }
    public List<internalsm_EventToken> getInternalsm_eventtokens() {
        return internalsm_eventtokens;
    }

    public void addInternalsm_eventtoken(Internalsm_eventtoken internalsm_eventtoken) {
        this.internalsm_eventtokens.add(internalsm_eventtoken);
    }

}