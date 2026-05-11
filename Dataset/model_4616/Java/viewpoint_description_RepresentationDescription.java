





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_RepresentationDescription extends description_DocumentedElement, description_EndUserDocumentedElement, description_IdentifiedElement {

    private String titleExpression;
    private boolean showOnStartup;
    private boolean initialisation;



    public viewpoint_description_RepresentationDescription(
        String titleExpression,        boolean showOnStartup,        boolean initialisation    ) {
        super(
        );
        this.titleExpression = titleExpression;
        this.showOnStartup = showOnStartup;
        this.initialisation = initialisation;
    }


    public String getTitleexpression() {
        return titleExpression;
    }

    public void setTitleexpression(String titleExpression) {
        this.titleExpression = titleExpression;
    }
    public boolean getShowonstartup() {
        return showOnStartup;
    }

    public void setShowonstartup(boolean showOnStartup) {
        this.showOnStartup = showOnStartup;
    }
    public boolean getInitialisation() {
        return initialisation;
    }

    public void setInitialisation(boolean initialisation) {
        this.initialisation = initialisation;
    }


}