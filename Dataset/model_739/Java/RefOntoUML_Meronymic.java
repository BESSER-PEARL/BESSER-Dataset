





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_Meronymic extends DirectedBinaryAssociation {

    private boolean isShareable;
    private boolean isImmutablePart;
    private boolean isImmutableWhole;
    private boolean isEssential;
    private boolean isInseparable;



    public RefOntoUML_Meronymic(
        boolean isShareable,        boolean isImmutablePart,        boolean isImmutableWhole,        boolean isEssential,        boolean isInseparable    ) {
        super(
        );
        this.isShareable = isShareable;
        this.isImmutablePart = isImmutablePart;
        this.isImmutableWhole = isImmutableWhole;
        this.isEssential = isEssential;
        this.isInseparable = isInseparable;
    }


    public boolean getIsshareable() {
        return isShareable;
    }

    public void setIsshareable(boolean isShareable) {
        this.isShareable = isShareable;
    }
    public boolean getIsimmutablepart() {
        return isImmutablePart;
    }

    public void setIsimmutablepart(boolean isImmutablePart) {
        this.isImmutablePart = isImmutablePart;
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
    public boolean getIsinseparable() {
        return isInseparable;
    }

    public void setIsinseparable(boolean isInseparable) {
        this.isInseparable = isInseparable;
    }


}