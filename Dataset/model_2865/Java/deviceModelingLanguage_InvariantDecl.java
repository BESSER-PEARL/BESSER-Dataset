





import java.util.List;
import java.util.ArrayList;

public class deviceModelingLanguage_InvariantDecl extends MemberDecl {

    private String invName;



    public deviceModelingLanguage_InvariantDecl(
        String invName    ) {
        super(
        );
        this.invName = invName;
    }


    public String getInvname() {
        return invName;
    }

    public void setInvname(String invName) {
        this.invName = invName;
    }


}