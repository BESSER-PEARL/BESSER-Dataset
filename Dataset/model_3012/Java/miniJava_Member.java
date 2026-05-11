





import java.util.List;
import java.util.ArrayList;

public class miniJava_Member extends TypedDeclaration {

    private String access;



    public miniJava_Member(
        String access    ) {
        super(
        );
        this.access = access;
    }


    public String getAccess() {
        return access;
    }

    public void setAccess(String access) {
        this.access = access;
    }


}