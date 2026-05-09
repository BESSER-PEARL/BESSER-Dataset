





import java.util.List;
import java.util.ArrayList;

public class baseCST_TemplateSignatureCS extends ModelElementCS {






    private baseCST_TemplateableElementCS basecst_templateableelementcs;




    private List<baseCST_TemplateParameterCS> basecst_templateparametercss;




    private baseCST_TemplateParameterCS basecst_templateparametercs;




    private baseCST_TemplateableElementCS basecst_templateableelementcs;


    public baseCST_TemplateSignatureCS(
    ) {
        super(
        );
        this.basecst_templateparametercss = new ArrayList<>();
    }

    public baseCST_TemplateSignatureCS(
        ArrayList<baseCST_TemplateParameterCS> basecst_templateparametercss    ) {
        this.basecst_templateparametercss = basecst_templateparametercss;
    }


    public baseCST_TemplateableElementCS getBasecst_templateableelementcs() {
        return basecst_templateableelementcs;
    }

    public void setBasecst_templateableelementcs(baseCST_TemplateableElementCS basecst_templateableelementcs) {
        this.basecst_templateableelementcs = basecst_templateableelementcs;
    }
    public List<baseCST_TemplateParameterCS> getBasecst_templateparametercss() {
        return basecst_templateparametercss;
    }

    public void addBasecst_templateparametercs(Basecst_templateparametercs basecst_templateparametercs) {
        this.basecst_templateparametercss.add(basecst_templateparametercs);
    }
    public baseCST_TemplateParameterCS getBasecst_templateparametercs() {
        return basecst_templateparametercs;
    }

    public void setBasecst_templateparametercs(baseCST_TemplateParameterCS basecst_templateparametercs) {
        this.basecst_templateparametercs = basecst_templateparametercs;
    }
    public baseCST_TemplateableElementCS getBasecst_templateableelementcs() {
        return basecst_templateableelementcs;
    }

    public void setBasecst_templateableelementcs(baseCST_TemplateableElementCS basecst_templateableelementcs) {
        this.basecst_templateableelementcs = basecst_templateableelementcs;
    }

}