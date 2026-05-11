





import java.util.List;
import java.util.ArrayList;

public class alf_ClassifierTemplateParameter  {

    private String comment;





    private alf_Name alf_name;




    private alf_TemplateParameters alf_templateparameters;




    private alf_QualifiedName alf_qualifiedname;


    public alf_ClassifierTemplateParameter(
        String comment    ) {
        this.comment = comment;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public alf_Name getAlf_name() {
        return alf_name;
    }

    public void setAlf_name(alf_Name alf_name) {
        this.alf_name = alf_name;
    }
    public alf_TemplateParameters getAlf_templateparameters() {
        return alf_templateparameters;
    }

    public void setAlf_templateparameters(alf_TemplateParameters alf_templateparameters) {
        this.alf_templateparameters = alf_templateparameters;
    }
    public alf_QualifiedName getAlf_qualifiedname() {
        return alf_qualifiedname;
    }

    public void setAlf_qualifiedname(alf_QualifiedName alf_qualifiedname) {
        this.alf_qualifiedname = alf_qualifiedname;
    }

}