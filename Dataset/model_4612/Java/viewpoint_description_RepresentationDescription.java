





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_RepresentationDescription extends description_EndUserDocumentedElement, description_IdentifiedElement, description_DocumentedElement {

    private boolean showOnStartup;
    private boolean initialisation;
    private String titleExpression;



    public viewpoint_description_RepresentationDescription(
        boolean showOnStartup,        boolean initialisation,        String titleExpression    ) {
        super(
        );
        this.showOnStartup = showOnStartup;
        this.initialisation = initialisation;
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
    public String getTitleexpression() {
        return titleExpression;
    }

    public void setTitleexpression(String titleExpression) {
        this.titleExpression = titleExpression;
    }


}