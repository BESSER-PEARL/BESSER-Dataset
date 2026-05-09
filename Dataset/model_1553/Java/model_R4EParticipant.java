





import java.util.List;
import java.util.ArrayList;

public class model_R4EParticipant extends R4EUser {

    private String focusArea;
    private boolean isPartOfDecision;
    private String roles;





    private model_R4EFormalReview model_r4eformalreview;


    public model_R4EParticipant(
        String focusArea,        boolean isPartOfDecision,        String roles    ) {
        super(
        );
        this.focusArea = focusArea;
        this.isPartOfDecision = isPartOfDecision;
        this.roles = roles;
    }


    public String getFocusarea() {
        return focusArea;
    }

    public void setFocusarea(String focusArea) {
        this.focusArea = focusArea;
    }
    public boolean getIspartofdecision() {
        return isPartOfDecision;
    }

    public void setIspartofdecision(boolean isPartOfDecision) {
        this.isPartOfDecision = isPartOfDecision;
    }
    public String getRoles() {
        return roles;
    }

    public void setRoles(String roles) {
        this.roles = roles;
    }

    public model_R4EFormalReview getModel_r4eformalreview() {
        return model_r4eformalreview;
    }

    public void setModel_r4eformalreview(model_R4EFormalReview model_r4eformalreview) {
        this.model_r4eformalreview = model_r4eformalreview;
    }

}