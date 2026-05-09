





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_Meronymic extends DirectedBinaryAssociation {

    private boolean isEssential;
    private boolean isInseparable;
    private boolean isImmutablePart;
    private boolean isShareable;
    private boolean isImmutableWhole;



    public RefOntoUML_Meronymic(
        boolean isEssential,        boolean isInseparable,        boolean isImmutablePart,        boolean isShareable,        boolean isImmutableWhole    ) {
        super(
        );
        this.isEssential = isEssential;
        this.isInseparable = isInseparable;
        this.isImmutablePart = isImmutablePart;
        this.isShareable = isShareable;
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
    public boolean getIsimmutablepart() {
        return isImmutablePart;
    }

    public void setIsimmutablepart(boolean isImmutablePart) {
        this.isImmutablePart = isImmutablePart;
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


}