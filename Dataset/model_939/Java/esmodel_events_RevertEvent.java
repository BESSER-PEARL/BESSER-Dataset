





import java.util.List;
import java.util.ArrayList;

public class esmodel_events_RevertEvent extends Event {

    private int revertedChangesCount;



    public esmodel_events_RevertEvent(
        int revertedChangesCount    ) {
        super(
        );
        this.revertedChangesCount = revertedChangesCount;
    }


    public int getRevertedchangescount() {
        return revertedChangesCount;
    }

    public void setRevertedchangescount(int revertedChangesCount) {
        this.revertedChangesCount = revertedChangesCount;
    }


}