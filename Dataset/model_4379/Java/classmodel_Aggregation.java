





import java.util.List;
import java.util.ArrayList;

public class classmodel_Aggregation extends Relationship {

    private boolean headNavigable;
    private String headLabel;
    private String tailLabel;
    private String tailVisibility;
    private String headVisibility;
    private boolean tailNavigable;



    public classmodel_Aggregation(
        boolean headNavigable,        String headLabel,        String tailLabel,        String tailVisibility,        String headVisibility,        boolean tailNavigable    ) {
        super(
        );
        this.headNavigable = headNavigable;
        this.headLabel = headLabel;
        this.tailLabel = tailLabel;
        this.tailVisibility = tailVisibility;
        this.headVisibility = headVisibility;
        this.tailNavigable = tailNavigable;
    }


    public boolean getHeadnavigable() {
        return headNavigable;
    }

    public void setHeadnavigable(boolean headNavigable) {
        this.headNavigable = headNavigable;
    }
    public String getHeadlabel() {
        return headLabel;
    }

    public void setHeadlabel(String headLabel) {
        this.headLabel = headLabel;
    }
    public String getTaillabel() {
        return tailLabel;
    }

    public void setTaillabel(String tailLabel) {
        this.tailLabel = tailLabel;
    }
    public String getTailvisibility() {
        return tailVisibility;
    }

    public void setTailvisibility(String tailVisibility) {
        this.tailVisibility = tailVisibility;
    }
    public String getHeadvisibility() {
        return headVisibility;
    }

    public void setHeadvisibility(String headVisibility) {
        this.headVisibility = headVisibility;
    }
    public boolean getTailnavigable() {
        return tailNavigable;
    }

    public void setTailnavigable(boolean tailNavigable) {
        this.tailNavigable = tailNavigable;
    }


}