





import java.util.List;
import java.util.ArrayList;

public class alf_Annotation  {

    private String args;
    private String kind;





    private alf_AnnotatedStatement alf_annotatedstatement;


    public alf_Annotation(
        String args,        String kind    ) {
        this.args = args;
        this.kind = kind;
    }


    public String getArgs() {
        return args;
    }

    public void setArgs(String args) {
        this.args = args;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public alf_AnnotatedStatement getAlf_annotatedstatement() {
        return alf_annotatedstatement;
    }

    public void setAlf_annotatedstatement(alf_AnnotatedStatement alf_annotatedstatement) {
        this.alf_annotatedstatement = alf_annotatedstatement;
    }

}