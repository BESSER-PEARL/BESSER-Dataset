





import java.util.List;
import java.util.ArrayList;

public class applauseDsl_ViewForAllSections  {






    private applauseDsl_ProviderConstruction applausedsl_providerconstruction;




    private applauseDsl_ScalarExpression applausedsl_scalarexpression;




    private List<applauseDsl_SectionCell> applausedsl_sectioncells;




    private applauseDsl_WebView applausedsl_webview;




    private applauseDsl_SectionedView applausedsl_sectionedview;


    public applauseDsl_ViewForAllSections(
    ) {
        this.applausedsl_sectioncells = new ArrayList<>();
    }

    public applauseDsl_ViewForAllSections(
        ArrayList<applauseDsl_SectionCell> applausedsl_sectioncells    ) {
        this.applausedsl_sectioncells = applausedsl_sectioncells;
    }


    public applauseDsl_ProviderConstruction getApplausedsl_providerconstruction() {
        return applausedsl_providerconstruction;
    }

    public void setApplausedsl_providerconstruction(applauseDsl_ProviderConstruction applausedsl_providerconstruction) {
        this.applausedsl_providerconstruction = applausedsl_providerconstruction;
    }
    public applauseDsl_ScalarExpression getApplausedsl_scalarexpression() {
        return applausedsl_scalarexpression;
    }

    public void setApplausedsl_scalarexpression(applauseDsl_ScalarExpression applausedsl_scalarexpression) {
        this.applausedsl_scalarexpression = applausedsl_scalarexpression;
    }
    public List<applauseDsl_SectionCell> getApplausedsl_sectioncells() {
        return applausedsl_sectioncells;
    }

    public void addApplausedsl_sectioncell(Applausedsl_sectioncell applausedsl_sectioncell) {
        this.applausedsl_sectioncells.add(applausedsl_sectioncell);
    }
    public applauseDsl_WebView getApplausedsl_webview() {
        return applausedsl_webview;
    }

    public void setApplausedsl_webview(applauseDsl_WebView applausedsl_webview) {
        this.applausedsl_webview = applausedsl_webview;
    }
    public applauseDsl_SectionedView getApplausedsl_sectionedview() {
        return applausedsl_sectionedview;
    }

    public void setApplausedsl_sectionedview(applauseDsl_SectionedView applausedsl_sectionedview) {
        this.applausedsl_sectionedview = applausedsl_sectionedview;
    }

}