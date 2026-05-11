





import java.util.List;
import java.util.ArrayList;

public class miniJava_TypeDeclaration extends NamedElement {

    private String accessLevel;



    public miniJava_TypeDeclaration(
        String accessLevel    ) {
        super(
        );
        this.accessLevel = accessLevel;
    }


    public String getAccesslevel() {
        return accessLevel;
    }

    public void setAccesslevel(String accessLevel) {
        this.accessLevel = accessLevel;
    }


}