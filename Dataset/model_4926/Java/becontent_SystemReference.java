





import java.util.List;
import java.util.ArrayList;

public class becontent_SystemReference extends SystemEntityField {

    private String name;





    private becontent_SystemEntity becontent_systementity;


    public becontent_SystemReference(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public becontent_SystemEntity getBecontent_systementity() {
        return becontent_systementity;
    }

    public void setBecontent_systementity(becontent_SystemEntity becontent_systementity) {
        this.becontent_systementity = becontent_systementity;
    }

}