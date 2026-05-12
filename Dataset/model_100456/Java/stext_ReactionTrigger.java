





import java.util.List;
import java.util.ArrayList;

public class stext_ReactionTrigger extends Trigger {






    private stext_Expression stext_expression;




    private List<stext_EventSpec> stext_eventspecs;


    public stext_ReactionTrigger(
    ) {
        super(
        );
        this.stext_eventspecs = new ArrayList<>();
    }

    public stext_ReactionTrigger(
        ArrayList<stext_EventSpec> stext_eventspecs    ) {
        this.stext_eventspecs = stext_eventspecs;
    }


    public stext_Expression getStext_expression() {
        return stext_expression;
    }

    public void setStext_expression(stext_Expression stext_expression) {
        this.stext_expression = stext_expression;
    }
    public List<stext_EventSpec> getStext_eventspecs() {
        return stext_eventspecs;
    }

    public void addStext_eventspec(Stext_eventspec stext_eventspec) {
        this.stext_eventspecs.add(stext_eventspec);
    }

}