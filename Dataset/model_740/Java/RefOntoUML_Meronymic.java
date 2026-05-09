





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_Meronymic extends DirectedBinaryAssociation {

    private boolean isImmutablePart;
    private boolean isEssential;
    private boolean isShareable;
    private boolean isInseparable;
    private boolean isImmutableWhole;



    public RefOntoUML_Meronymic(
        boolean isImmutablePart,        boolean isEssential,        boolean isShareable,        boolean isInseparable,        boolean isImmutableWhole    ) {
        super(
        );
        this.isImmutablePart = isImmutablePart;
        this.isEssential = isEssential;
        this.isShareable = isShareable;
        this.isInseparable = isInseparable;
        this.isImmutableWhole = isImmutableWhole;
    }


    public boolean getIsimmutablepart() {
        return isImmutablePart;
    }

    public void setIsimmutablepart(boolean isImmutablePart) {
        this.isImmutablePart = isImmutablePart;
    }
    public boolean getIsessential() {
        return isEssential;
    }

    public void setIsessential(boolean isEssential) {
        this.isEssential = isEssential;
    }
    public boolean getIsshareable() {
        return isShareable;
    }

    public void setIsshareable(boolean isShareable) {
        this.isShareable = isShareable;
    }
    public boolean getIsinseparable() {
        return isInseparable;
    }

    public void setIsinseparable(boolean isInseparable) {
        this.isInseparable = isInseparable;
    }
    public boolean getIsimmutablewhole() {
        return isImmutableWhole;
    }

    public void setIsimmutablewhole(boolean isImmutableWhole) {
        this.isImmutableWhole = isImmutableWhole;
    }


}