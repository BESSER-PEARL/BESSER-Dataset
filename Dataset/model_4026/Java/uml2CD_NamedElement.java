





import java.util.List;
import java.util.ArrayList;

public class uml2CD_NamedElement  {

    private String name;





    private uml2CD_Comment uml2cd_comment;


    public uml2CD_NamedElement(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public uml2CD_Comment getUml2cd_comment() {
        return uml2cd_comment;
    }

    public void setUml2cd_comment(uml2CD_Comment uml2cd_comment) {
        this.uml2cd_comment = uml2cd_comment;
    }

}