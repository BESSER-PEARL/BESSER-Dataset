





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_RepresentationDescription extends description_DocumentedElement, description_IdentifiedElement, description_EndUserDocumentedElement {

    private String titleExpression;
    private boolean initialisation;
    private boolean showOnStartup;



    public viewpoint_description_RepresentationDescription(
        String titleExpression,        boolean initialisation,        boolean showOnStartup    ) {
        super(
        );
        this.titleExpression = titleExpression;
        this.initialisation = initialisation;
        this.showOnStartup = showOnStartup;
    }


    public String getTitleexpression() {
        return titleExpression;
    }

    public void setTitleexpression(String titleExpression) {
        this.titleExpression = titleExpression;
    }
    public boolean getInitialisation() {
        return initialisation;
    }

    public void setInitialisation(boolean initialisation) {
        this.initialisation = initialisation;
    }
    public boolean getShowonstartup() {
        return showOnStartup;
    }

    public void setShowonstartup(boolean showOnStartup) {
        this.showOnStartup = showOnStartup;
    }


}