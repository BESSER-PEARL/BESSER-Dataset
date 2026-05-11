





import java.util.List;
import java.util.ArrayList;

public class applauseDsl_UIActionNavigateAction extends UIActionSpecification {

    private String actionVerb;





    private applauseDsl_ReferrableElement applausedsl_referrableelement;




    private applauseDsl_Screen applausedsl_screen;


    public applauseDsl_UIActionNavigateAction(
        String actionVerb    ) {
        super(
        );
        this.actionVerb = actionVerb;
    }


    public String getActionverb() {
        return actionVerb;
    }

    public void setActionverb(String actionVerb) {
        this.actionVerb = actionVerb;
    }

    public applauseDsl_ReferrableElement getApplausedsl_referrableelement() {
        return applausedsl_referrableelement;
    }

    public void setApplausedsl_referrableelement(applauseDsl_ReferrableElement applausedsl_referrableelement) {
        this.applausedsl_referrableelement = applausedsl_referrableelement;
    }
    public applauseDsl_Screen getApplausedsl_screen() {
        return applausedsl_screen;
    }

    public void setApplausedsl_screen(applauseDsl_Screen applausedsl_screen) {
        this.applausedsl_screen = applausedsl_screen;
    }

}