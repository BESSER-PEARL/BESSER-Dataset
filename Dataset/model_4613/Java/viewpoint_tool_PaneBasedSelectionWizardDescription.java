





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_PaneBasedSelectionWizardDescription extends AbstractToolDescription {

    private String selectedValuesMessage;
    private String candidatesExpression;
    private String iconPath;
    private String choiceOfValuesMessage;
    private String preSelectedCandidatesExpression;
    private String message;
    private String childrenExpression;
    private String windowImagePath;
    private boolean tree;
    private String windowTitle;
    private String rootExpression;





    private tool_InitialOperation tool_initialoperation;


    public viewpoint_tool_PaneBasedSelectionWizardDescription(
        String selectedValuesMessage,        String candidatesExpression,        String iconPath,        String choiceOfValuesMessage,        String preSelectedCandidatesExpression,        String message,        String childrenExpression,        String windowImagePath,        boolean tree,        String windowTitle,        String rootExpression    ) {
        super(
        );
        this.selectedValuesMessage = selectedValuesMessage;
        this.candidatesExpression = candidatesExpression;
        this.iconPath = iconPath;
        this.choiceOfValuesMessage = choiceOfValuesMessage;
        this.preSelectedCandidatesExpression = preSelectedCandidatesExpression;
        this.message = message;
        this.childrenExpression = childrenExpression;
        this.windowImagePath = windowImagePath;
        this.tree = tree;
        this.windowTitle = windowTitle;
        this.rootExpression = rootExpression;
    }


    public String getSelectedvaluesmessage() {
        return selectedValuesMessage;
    }

    public void setSelectedvaluesmessage(String selectedValuesMessage) {
        this.selectedValuesMessage = selectedValuesMessage;
    }
    public String getCandidatesexpression() {
        return candidatesExpression;
    }

    public void setCandidatesexpression(String candidatesExpression) {
        this.candidatesExpression = candidatesExpression;
    }
    public String getIconpath() {
        return iconPath;
    }

    public void setIconpath(String iconPath) {
        this.iconPath = iconPath;
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
    public String getWindowimagepath() {
        return windowImagePath;
    }

    public void setWindowimagepath(String windowImagePath) {
        this.windowImagePath = windowImagePath;
    }
    public boolean getTree() {
        return tree;
    }

    public void setTree(boolean tree) {
        this.tree = tree;
    }
    public String getWindowtitle() {
        return windowTitle;
    }

    public void setWindowtitle(String windowTitle) {
        this.windowTitle = windowTitle;
    }
    public String getRootexpression() {
        return rootExpression;
    }

    public void setRootexpression(String rootExpression) {
        this.rootExpression = rootExpression;
    }

    public tool_InitialOperation getTool_initialoperation() {
        return tool_initialoperation;
    }

    public void setTool_initialoperation(tool_InitialOperation tool_initialoperation) {
        this.tool_initialoperation = tool_initialoperation;
    }

}