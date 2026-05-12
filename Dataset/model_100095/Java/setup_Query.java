





import java.util.List;
import java.util.ArrayList;

public class setup_Query  {

    private String summary;
    private String uRL;





    private setup_MylynQueriesTask setup_mylynqueriestask;




    private setup_MylynQueriesTask setup_mylynqueriestask;




    private List<setup_QueryAttribute> setup_queryattributes;


    public setup_Query(
        String summary,        String uRL    ) {
        this.summary = summary;
        this.uRL = uRL;
        this.setup_queryattributes = new ArrayList<>();
    }

    public setup_Query(
        String summary,        String uRL        ArrayList<setup_QueryAttribute> setup_queryattributes    ) {
        this.summary = summary;
        this.uRL = uRL;
        this.setup_queryattributes = setup_queryattributes;
    }

    public String getSummary() {
        return summary;
    }

    public void setSummary(String summary) {
        this.summary = summary;
    }
    public String getUrl() {
        return uRL;
    }

    public void setUrl(String uRL) {
        this.uRL = uRL;
    }

    public setup_MylynQueriesTask getSetup_mylynqueriestask() {
        return setup_mylynqueriestask;
    }

    public void setSetup_mylynqueriestask(setup_MylynQueriesTask setup_mylynqueriestask) {
        this.setup_mylynqueriestask = setup_mylynqueriestask;
    }
    public setup_MylynQueriesTask getSetup_mylynqueriestask() {
        return setup_mylynqueriestask;
    }

    public void setSetup_mylynqueriestask(setup_MylynQueriesTask setup_mylynqueriestask) {
        this.setup_mylynqueriestask = setup_mylynqueriestask;
    }
    public List<setup_QueryAttribute> getSetup_queryattributes() {
        return setup_queryattributes;
    }

    public void addSetup_queryattribute(Setup_queryattribute setup_queryattribute) {
        this.setup_queryattributes.add(setup_queryattribute);
    }

}