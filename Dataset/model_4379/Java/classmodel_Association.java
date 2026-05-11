





import java.util.List;
import java.util.ArrayList;

public class classmodel_Association extends Relationship {

    private boolean headNavigable;
    private String headVisibility;
    private boolean tailNavigable;
    private String tailVisibility;
    private String tailLabel;
    private String headLabel;



    public classmodel_Association(
        boolean headNavigable,        String headVisibility,        boolean tailNavigable,        String tailVisibility,        String tailLabel,        String headLabel    ) {
        super(
        );
        this.headNavigable = headNavigable;
        this.headVisibility = headVisibility;
        this.tailNavigable = tailNavigable;
        this.tailVisibility = tailVisibility;
        this.tailLabel = tailLabel;
        this.headLabel = headLabel;
    }


    public boolean getHeadnavigable() {
        return headNavigable;
    }

    public void setHeadnavigable(boolean headNavigable) {
        this.headNavigable = headNavigable;
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
    public String getTailvisibility() {
        return tailVisibility;
    }

    public void setTailvisibility(String tailVisibility) {
        this.tailVisibility = tailVisibility;
    }
    public String getTaillabel() {
        return tailLabel;
    }

    public void setTaillabel(String tailLabel) {
        this.tailLabel = tailLabel;
    }
    public String getHeadlabel() {
        return headLabel;
    }

    public void setHeadlabel(String headLabel) {
        this.headLabel = headLabel;
    }


}