





import java.util.List;
import java.util.ArrayList;

public class classmodel_Composition extends Relationship {

    private String tailVisibility;
    private boolean headNavigable;
    private String headVisibility;
    private String tailLabel;
    private boolean tailNavigable;
    private String headLabel;



    public classmodel_Composition(
        String tailVisibility,        boolean headNavigable,        String headVisibility,        String tailLabel,        boolean tailNavigable,        String headLabel    ) {
        super(
        );
        this.tailVisibility = tailVisibility;
        this.headNavigable = headNavigable;
        this.headVisibility = headVisibility;
        this.tailLabel = tailLabel;
        this.tailNavigable = tailNavigable;
        this.headLabel = headLabel;
    }


    public String getTailvisibility() {
        return tailVisibility;
    }

    public void setTailvisibility(String tailVisibility) {
        this.tailVisibility = tailVisibility;
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
    public String getTaillabel() {
        return tailLabel;
    }

    public void setTaillabel(String tailLabel) {
        this.tailLabel = tailLabel;
    }
    public boolean getTailnavigable() {
        return tailNavigable;
    }

    public void setTailnavigable(boolean tailNavigable) {
        this.tailNavigable = tailNavigable;
    }
    public String getHeadlabel() {
        return headLabel;
    }

    public void setHeadlabel(String headLabel) {
        this.headLabel = headLabel;
    }


}