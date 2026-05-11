





import java.util.List;
import java.util.ArrayList;

public class diva_Configuration extends ScoredElement {

    private String verdict;





    private diva_Context diva_context;


    public diva_Configuration(
        String verdict    ) {
        super(
        );
        this.verdict = verdict;
    }


    public String getVerdict() {
        return verdict;
    }

    public void setVerdict(String verdict) {
        this.verdict = verdict;
    }

    public diva_Context getDiva_context() {
        return diva_context;
    }

    public void setDiva_context(diva_Context diva_context) {
        this.diva_context = diva_context;
    }

}