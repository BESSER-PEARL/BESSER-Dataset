





import java.util.List;
import java.util.ArrayList;

public class esmodel_events_LinkEvent extends Event {

    private String sourceView;
    private boolean createdNew;



    public esmodel_events_LinkEvent(
        String sourceView,        boolean createdNew    ) {
        super(
        );
        this.sourceView = sourceView;
        this.createdNew = createdNew;
    }


    public String getSourceview() {
        return sourceView;
    }

    public void setSourceview(String sourceView) {
        this.sourceView = sourceView;
    }
    public boolean getCreatednew() {
        return createdNew;
    }

    public void setCreatednew(boolean createdNew) {
        this.createdNew = createdNew;
    }


}