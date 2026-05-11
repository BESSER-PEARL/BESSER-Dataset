





import java.util.List;
import java.util.ArrayList;

public class alf_NamedTemplateBinding  {

    private String formal;





    private alf_TemplateBinding alf_templatebinding;




    private alf_QualifiedNameWithBinding alf_qualifiednamewithbinding;


    public alf_NamedTemplateBinding(
        String formal    ) {
        this.formal = formal;
    }


    public String getFormal() {
        return formal;
    }

    public void setFormal(String formal) {
        this.formal = formal;
    }

    public alf_TemplateBinding getAlf_templatebinding() {
        return alf_templatebinding;
    }

    public void setAlf_templatebinding(alf_TemplateBinding alf_templatebinding) {
        this.alf_templatebinding = alf_templatebinding;
    }
    public alf_QualifiedNameWithBinding getAlf_qualifiednamewithbinding() {
        return alf_qualifiednamewithbinding;
    }

    public void setAlf_qualifiednamewithbinding(alf_QualifiedNameWithBinding alf_qualifiednamewithbinding) {
        this.alf_qualifiednamewithbinding = alf_qualifiednamewithbinding;
    }

}