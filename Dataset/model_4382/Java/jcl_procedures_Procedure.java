





import java.util.List;
import java.util.ArrayList;

public class jcl_procedures_Procedure extends containers_JCLRoot, members_Member, commons_NamedElement {

    private String endName;



    public jcl_procedures_Procedure(
        String endName    ) {
        super(
        );
        this.endName = endName;
    }


    public String getEndname() {
        return endName;
    }

    public void setEndname(String endName) {
        this.endName = endName;
    }


}