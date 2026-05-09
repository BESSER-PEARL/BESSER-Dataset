





import java.util.List;
import java.util.ArrayList;

public class esmodel_events_MergeGlobalChoiceEvent extends Event {

    private String selection;



    public esmodel_events_MergeGlobalChoiceEvent(
        String selection    ) {
        super(
        );
        this.selection = selection;
    }


    public String getSelection() {
        return selection;
    }

    public void setSelection(String selection) {
        this.selection = selection;
    }


}