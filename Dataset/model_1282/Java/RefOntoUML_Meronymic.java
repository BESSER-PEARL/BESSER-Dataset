





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_Meronymic extends DirectedBinaryAssociation {

    private boolean isShareable;
    private boolean isImmutableWhole;
    private boolean isEssential;
    private boolean isImmutablePart;
    private boolean isInseparable;



    public RefOntoUML_Meronymic(
        boolean isShareable,        boolean isImmutableWhole,        boolean isEssential,        boolean isImmutablePart,        boolean isInseparable    ) {
        super(
        );
        this.isShareable = isShareable;
        this.isImmutableWhole = isImmutableWhole;
        this.isEssential = isEssential;
        this.isImmutablePart = isImmutablePart;
        this.isInseparable = isInseparable;
    }


    public boolean getIsshareable() {
        return isShareable;
    }

    public void setIsshareable(boolean isShareable) {
        this.isShareable = isShareable;
    }
    public boolean getIsimmutablewhole() {
        return isImmutableWhole;
    }

    public void setIsimmutablewhole(boolean isImmutableWhole) {
        this.isImmutableWhole = isImmutableWhole;
    }
    public boolean getIsessential() {
        return isEssential;
    }

    public void setIsessential(boolean isEssential) {
        this.isEssential = isEssential;
    }
    public boolean getIsimmutablepart() {
        return isImmutablePart;
    }

    public void setIsimmutablepart(boolean isImmutablePart) {
        this.isImmutablePart = isImmutablePart;
    }
    public boolean getIsinseparable() {
        return isInseparable;
    }

    public void setIsinseparable(boolean isInseparable) {
        this.isInseparable = isInseparable;
    }


}