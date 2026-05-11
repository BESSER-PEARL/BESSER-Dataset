





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_RepresentationDescription extends description_IdentifiedElement, description_EndUserDocumentedElement, description_DocumentedElement {

    private boolean showOnStartup;
    private String titleExpression;
    private boolean initialisation;



    public viewpoint_description_RepresentationDescription(
        boolean showOnStartup,        String titleExpression,        boolean initialisation    ) {
        super(
        );
        this.showOnStartup = showOnStartup;
        this.titleExpression = titleExpression;
        this.initialisation = initialisation;
    }


    public boolean getShowonstartup() {
        return showOnStartup;
    }

    public void setShowonstartup(boolean showOnStartup) {
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


}