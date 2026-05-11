





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_PaneBasedSelectionWizardDescription extends AbstractToolDescription {

    private String preSelectedCandidatesExpression;
    private String iconPath;
    private String windowTitle;
    private String message;
    private String rootExpression;
    private String choiceOfValuesMessage;
    private boolean tree;
    private String childrenExpression;
    private String candidatesExpression;
    private String windowImagePath;
    private String selectedValuesMessage;



    public viewpoint_tool_PaneBasedSelectionWizardDescription(
        String preSelectedCandidatesExpression,        String iconPath,        String windowTitle,        String message,        String rootExpression,        String choiceOfValuesMessage,        boolean tree,        String childrenExpression,        String candidatesExpression,        String windowImagePath,        String selectedValuesMessage    ) {
        super(
        );
        this.preSelectedCandidatesExpression = preSelectedCandidatesExpression;
        this.iconPath = iconPath;
        this.windowTitle = windowTitle;
        this.message = message;
        this.rootExpression = rootExpression;
        this.choiceOfValuesMessage = choiceOfValuesMessage;
        this.tree = tree;
        this.childrenExpression = childrenExpression;
        this.candidatesExpression = candidatesExpression;
        this.windowImagePath = windowImagePath;
        this.selectedValuesMessage = selectedValuesMessage;
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
    public String getChildrenexpression() {
        return childrenExpression;
    }

    public void setChildrenexpression(String childrenExpression) {
        this.childrenExpression = childrenExpression;
    }
    public String getCandidatesexpression() {
        return candidatesExpression;
    }

    public void setCandidatesexpression(String candidatesExpression) {
        this.candidatesExpression = candidatesExpression;
    }
    public String getWindowimagepath() {
        return windowImagePath;
    }

    public void setWindowimagepath(String windowImagePath) {
        this.windowImagePath = windowImagePath;
    }
    public String getSelectedvaluesmessage() {
        return selectedValuesMessage;
    }

    public void setSelectedvaluesmessage(String selectedValuesMessage) {
        this.selectedValuesMessage = selectedValuesMessage;
    }


}