





import java.util.List;
import java.util.ArrayList;

public class alf_FormalParameter  {

    private String comment;
    private String parameterDirection;





    private alf_FormalParameterList alf_formalparameterlist;




    private alf_Name alf_name;




    private alf_StereotypeAnnotations alf_stereotypeannotations;


    public alf_FormalParameter(
        String comment,        String parameterDirection    ) {
        this.comment = comment;
        this.parameterDirection = parameterDirection;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getParameterdirection() {
        return parameterDirection;
    }

    public void setParameterdirection(String parameterDirection) {
        this.parameterDirection = parameterDirection;
    }

    public alf_FormalParameterList getAlf_formalparameterlist() {
        return alf_formalparameterlist;
    }

    public void setAlf_formalparameterlist(alf_FormalParameterList alf_formalparameterlist) {
        this.alf_formalparameterlist = alf_formalparameterlist;
    }
    public alf_Name getAlf_name() {
        return alf_name;
    }

    public void setAlf_name(alf_Name alf_name) {
        this.alf_name = alf_name;
    }
    public alf_StereotypeAnnotations getAlf_stereotypeannotations() {
        return alf_stereotypeannotations;
    }

    public void setAlf_stereotypeannotations(alf_StereotypeAnnotations alf_stereotypeannotations) {
        this.alf_stereotypeannotations = alf_stereotypeannotations;
    }

}