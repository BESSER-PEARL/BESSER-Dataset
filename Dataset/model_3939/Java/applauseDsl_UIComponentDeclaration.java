





import java.util.List;
import java.util.ArrayList;

public class applauseDsl_UIComponentDeclaration extends NamedElement, UIComponentOrDataType {






    private List<applauseDsl_UIComponentMemberDeclaration> applausedsl_uicomponentmemberdeclarations;


    public applauseDsl_UIComponentDeclaration(
    ) {
        super(
        );
        this.applausedsl_uicomponentmemberdeclarations = new ArrayList<>();
    }

    public applauseDsl_UIComponentDeclaration(
        ArrayList<applauseDsl_UIComponentMemberDeclaration> applausedsl_uicomponentmemberdeclarations    ) {
        this.applausedsl_uicomponentmemberdeclarations = applausedsl_uicomponentmemberdeclarations;
    }


    public List<applauseDsl_UIComponentMemberDeclaration> getApplausedsl_uicomponentmemberdeclarations() {
        return applausedsl_uicomponentmemberdeclarations;
    }

    public void addApplausedsl_uicomponentmemberdeclaration(Applausedsl_uicomponentmemberdeclaration applausedsl_uicomponentmemberdeclaration) {
        this.applausedsl_uicomponentmemberdeclarations.add(applausedsl_uicomponentmemberdeclaration);
    }

}