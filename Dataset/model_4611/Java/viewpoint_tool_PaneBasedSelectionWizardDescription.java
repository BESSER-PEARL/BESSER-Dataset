





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_PaneBasedSelectionWizardDescription extends AbstractToolDescription {

    private String childrenExpression;
    private String windowImagePath;
    private String rootExpression;
    private String choiceOfValuesMessage;
    private boolean tree;
    private String candidatesExpression;
    private String selectedValuesMessage;
    private String iconPath;
    private String preSelectedCandidatesExpression;
    private String message;
    private String windowTitle;



    public viewpoint_tool_PaneBasedSelectionWizardDescription(
        String childrenExpression,        String windowImagePath,        String rootExpression,        String choiceOfValuesMessage,        boolean tree,        String candidatesExpression,        String selectedValuesMessage,        String iconPath,        String preSelectedCandidatesExpression,        String message,        String windowTitle    ) {
        super(
        );
        this.childrenExpression = childrenExpression;
        this.windowImagePath = windowImagePath;
        this.rootExpression = rootExpression;
        this.choiceOfValuesMessage = choiceOfValuesMessage;
        this.tree = tree;
        this.candidatesExpression = candidatesExpression;
        this.selectedValuesMessage = selectedValuesMessage;
        this.iconPath = iconPath;
        this.preSelectedCandidatesExpression = preSelectedCandidatesExpression;
        this.message = message;
        this.windowTitle = windowTitle;
    }


    public String getChildrenexpression() {
        return childrenExpression;
    }

    public void setChildrenexpression(String childrenExpression) {
        this.childrenExpression = childrenExpression;
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
    public String getChoiceofvaluesmessage() {
        return choiceOfValuesMessage;
    }

    public void setChoiceofvaluesmessage(String choiceOfValuesMessage) {
        this.choiceOfValuesMessage = choiceOfValuesMessage;
    }
    public boolean getTree() {
        return tree;
    }

    public void setTree(boolean tree) {
        this.tree = tree;
    }
    public String getCandidatesexpression() {
        return candidatesExpression;
    }

    public void setCandidatesexpression(String candidatesExpression) {
        this.candidatesExpression = candidatesExpression;
    }
    public String getSelectedvaluesmessage() {
        return selectedValuesMessage;
    }

    public void setSelectedvaluesmessage(String selectedValuesMessage) {
        this.selectedValuesMessage = selectedValuesMessage;
    }
    public String getIconpath() {
        return iconPath;
    }

    public void setIconpath(String iconPath) {
        this.iconPath = iconPath;
    }
    public String getPreselectedcandidatesexpression() {
        return preSelectedCandidatesExpression;
    }

    public void setPreselectedcandidatesexpression(String preSelectedCandidatesExpression) {
        this.preSelectedCandidatesExpression = preSelectedCandidatesExpression;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getWindowtitle() {
        return windowTitle;
    }

    public void setWindowtitle(String windowTitle) {
        this.windowTitle = windowTitle;
    }


}