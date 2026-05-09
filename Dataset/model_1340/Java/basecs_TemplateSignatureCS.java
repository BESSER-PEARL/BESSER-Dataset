





import java.util.List;
import java.util.ArrayList;

public class basecs_TemplateSignatureCS extends ModelElementCS {






    private basecs_TemplateableElementCS basecs_templateableelementcs;




    private basecs_TemplateableElementCS basecs_templateableelementcs;




    private List<basecs_TemplateParameterCS> basecs_templateparametercss;




    private basecs_TemplateParameterCS basecs_templateparametercs;


    public basecs_TemplateSignatureCS(
    ) {
        super(
        );
        this.basecs_templateparametercss = new ArrayList<>();
    }

    public basecs_TemplateSignatureCS(
        ArrayList<basecs_TemplateParameterCS> basecs_templateparametercss    ) {
        this.basecs_templateparametercss = basecs_templateparametercss;
    }


    public basecs_TemplateableElementCS getBasecs_templateableelementcs() {
        return basecs_templateableelementcs;
    }

    public void setBasecs_templateableelementcs(basecs_TemplateableElementCS basecs_templateableelementcs) {
        this.basecs_templateableelementcs = basecs_templateableelementcs;
    }
    public basecs_TemplateableElementCS getBasecs_templateableelementcs() {
        return basecs_templateableelementcs;
    }

    public void setBasecs_templateableelementcs(basecs_TemplateableElementCS basecs_templateableelementcs) {
        this.basecs_templateableelementcs = basecs_templateableelementcs;
    }
    public List<basecs_TemplateParameterCS> getBasecs_templateparametercss() {
        return basecs_templateparametercss;
    }

    public void addBasecs_templateparametercs(Basecs_templateparametercs basecs_templateparametercs) {
        this.basecs_templateparametercss.add(basecs_templateparametercs);
    }
    public basecs_TemplateParameterCS getBasecs_templateparametercs() {
        return basecs_templateparametercs;
    }

    public void setBasecs_templateparametercs(basecs_TemplateParameterCS basecs_templateparametercs) {
        this.basecs_templateparametercs = basecs_templateparametercs;
    }

}