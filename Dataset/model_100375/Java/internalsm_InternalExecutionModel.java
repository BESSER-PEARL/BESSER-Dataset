





import java.util.List;
import java.util.ArrayList;

public class internalsm_InternalExecutionModel  {

    private String context;





    private List<internalsm_EventToken> internalsm_eventtokens;


    public internalsm_InternalExecutionModel(
        String context    ) {
        this.context = context;
        this.internalsm_eventtokens = new ArrayList<>();
    }

    public internalsm_InternalExecutionModel(
        String context        ArrayList<internalsm_EventToken> internalsm_eventtokens    ) {
        this.context = context;
        this.internalsm_eventtokens = internalsm_eventtokens;
    }

    public String getContext() {
        return context;
    }

    public void setContext(String context) {
        this.context = context;
    }

    public List<internalsm_EventToken> getInternalsm_eventtokens() {
        return internalsm_eventtokens;
    }

    public void addInternalsm_eventtoken(Internalsm_eventtoken internalsm_eventtoken) {
        this.internalsm_eventtokens.add(internalsm_eventtoken);
    }

}