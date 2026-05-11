





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_PaneBasedSelectionWizardDescription extends AbstractToolDescription {

    private boolean tree;
    private String windowImagePath;
    private String rootExpression;
    private String windowTitle;
    private String message;
    private String candidatesExpression;
    private String childrenExpression;
    private String selectedValuesMessage;
    private String choiceOfValuesMessage;
    private String preSelectedCandidatesExpression;
    private String iconPath;



    public viewpoint_tool_PaneBasedSelectionWizardDescription(
        boolean tree,        String windowImagePath,        String rootExpression,        String windowTitle,        String message,        String candidatesExpression,        String childrenExpression,        String selectedValuesMessage,        String choiceOfValuesMessage,        String preSelectedCandidatesExpression,        String iconPath    ) {
        super(
        );
        this.tree = tree;
        this.windowImagePath = windowImagePath;
        this.rootExpression = rootExpression;
        this.windowTitle = windowTitle;
        this.message = message;
        this.candidatesExpression = candidatesExpression;
        this.childrenExpression = childrenExpression;
        this.selectedValuesMessage = selectedValuesMessage;
        this.choiceOfValuesMessage = choiceOfValuesMessage;
        this.preSelectedCandidatesExpression = preSelectedCandidatesExpression;
        this.iconPath = iconPath;
    }


    public boolean getTree() {
        return tree;
    }

    public void setTree(boolean tree) {
        this.tree = tree;
    }
    public String getWindowimagepath() {
        return windowImagePath;
    }

    public void setWindowimagepath(String windowImagePath) {
        this.windowImagePath = windowImagePath;
    }
    public String getRootexpression() {
        return rootExpression;
    }

    public void setRootexpression(String rootExpression) {
        this.rootExpression = rootExpression;
    }
    public String getWindowtitle() {
        return windowTitle;
    }

    public void setWindowtitle(String windowTitle) {
        this.windowTitle = windowTitle;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getCandidatesexpression() {
        return candidatesExpression;
    }

    public void setCandidatesexpression(String candidatesExpression) {
        this.candidatesExpression = candidatesExpression;
    }
    public String getChildrenexpression() {
        return childrenExpression;
    }

    public void setChildrenexpression(String childrenExpression) {
        this.childrenExpression = childrenExpression;
    }
    public String getSelectedvaluesmessage() {
        return selectedValuesMessage;
    }

    public void setSelectedvaluesmessage(String selectedValuesMessage) {
        this.selectedValuesMessage = selectedValuesMessage;
    }
    public String getChoiceofvaluesmessage() {
        return choiceOfValuesMessage;
    }

    public void setChoiceofvaluesmessage(String choiceOfValuesMessage) {
        this.choiceOfValuesMessage = choiceOfValuesMessage;
    }
    public String getPreselectedcandidatesexpression() {
        return preSelectedCandidatesExpression;
    }

    public void setPreselectedcandidatesexpression(String preSelectedCandidatesExpression) {
        this.preSelectedCandidatesExpression = preSelectedCandidatesExpression;
    }
    public String getIconpath() {
        return iconPath;
    }

    public void setIconpath(String iconPath) {
        this.iconPath = iconPath;
    }


}