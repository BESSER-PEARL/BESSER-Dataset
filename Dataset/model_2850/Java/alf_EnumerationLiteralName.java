





import java.util.List;
import java.util.ArrayList;

public class alf_EnumerationLiteralName  {

    private String comment;





    private alf_Name alf_name;




    private alf_EnumerationBody alf_enumerationbody;


    public alf_EnumerationLiteralName(
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
    public alf_EnumerationBody getAlf_enumerationbody() {
        return alf_enumerationbody;
    }

    public void setAlf_enumerationbody(alf_EnumerationBody alf_enumerationbody) {
        this.alf_enumerationbody = alf_enumerationbody;
    }

}