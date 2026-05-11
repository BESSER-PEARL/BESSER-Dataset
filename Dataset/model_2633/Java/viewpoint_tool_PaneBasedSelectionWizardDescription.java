





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_PaneBasedSelectionWizardDescription extends AbstractToolDescription {

    private String preSelectedCandidatesExpression;
    private String candidatesExpression;
    private String windowTitle;
    private String choiceOfValuesMessage;
    private String selectedValuesMessage;
    private String windowImagePath;
    private String iconPath;
    private boolean tree;
    private String message;
    private String childrenExpression;
    private String rootExpression;



    public viewpoint_tool_PaneBasedSelectionWizardDescription(
        String preSelectedCandidatesExpression,        String candidatesExpression,        String windowTitle,        String choiceOfValuesMessage,        String selectedValuesMessage,        String windowImagePath,        String iconPath,        boolean tree,        String message,        String childrenExpression,        String rootExpression    ) {
        super(
        );
        this.preSelectedCandidatesExpression = preSelectedCandidatesExpression;
        this.candidatesExpression = candidatesExpression;
        this.windowTitle = windowTitle;
        this.choiceOfValuesMessage = choiceOfValuesMessage;
        this.selectedValuesMessage = selectedValuesMessage;
        this.windowImagePath = windowImagePath;
        this.iconPath = iconPath;
        this.tree = tree;
        this.message = message;
        this.childrenExpression = childrenExpression;
        this.rootExpression = rootExpression;
    }


    public String getPreselectedcandidatesexpression() {
        return preSelectedCandidatesExpression;
    }

    public void setPreselectedcandidatesexpression(String preSelectedCandidatesExpression) {
        this.preSelectedCandidatesExpression = preSelectedCandidatesExpression;
    }
    public String getCandidatesexpression() {
        return candidatesExpression;
    }

    public void setCandidatesexpression(String candidatesExpression) {
        this.candidatesExpression = candidatesExpression;
    }
    public String getWindowtitle() {
        return windowTitle;
    }

    public void setWindowtitle(String windowTitle) {
        this.windowTitle = windowTitle;
    }
    public String getChoiceofvaluesmessage() {
        return choiceOfValuesMessage;
    }

    public void setChoiceofvaluesmessage(String choiceOfValuesMessage) {
        this.choiceOfValuesMessage = choiceOfValuesMessage;
    }
    public String getSelectedvaluesmessage() {
        return selectedValuesMessage;
    }

    public void setSelectedvaluesmessage(String selectedValuesMessage) {
        this.selectedValuesMessage = selectedValuesMessage;
    }
    public String getWindowimagepath() {
        return windowImagePath;
    }

    public void setWindowimagepath(String windowImagePath) {
        this.windowImagePath = windowImagePath;
    }
    public String getIconpath() {
        return iconPath;
    }

    public void setIconpath(String iconPath) {
        this.iconPath = iconPath;
    }
    public boolean getTree() {
        return tree;
    }

    public void setTree(boolean tree) {
        this.tree = tree;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getChildrenexpression() {
        return childrenExpression;
    }

    public void setChildrenexpression(String childrenExpression) {
        this.childrenExpression = childrenExpression;
    }
    public String getRootexpression() {
        return rootExpression;
    }

    public void setRootexpression(String rootExpression) {
        this.rootExpression = rootExpression;
    }


}