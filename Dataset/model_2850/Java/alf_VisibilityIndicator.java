





import java.util.List;
import java.util.ArrayList;

public class alf_VisibilityIndicator  {

    private String PUBLIC;
    private String PRIVATE;
    private String PROTECTED;



    public alf_VisibilityIndicator(
        String PUBLIC,        String PRIVATE,        String PROTECTED    ) {
        this.PUBLIC = PUBLIC;
        this.PRIVATE = PRIVATE;
        this.PROTECTED = PROTECTED;
    }


    public String getPublic() {
        return PUBLIC;
    }

    public void setPublic(String PUBLIC) {
        this.PUBLIC = PUBLIC;
    }
    public String getPrivate() {
        return PRIVATE;
    }

    public void setPrivate(String PRIVATE) {
        this.PRIVATE = PRIVATE;
    }
    public String getProtected() {
        return PROTECTED;
    }

    public void setProtected(String PROTECTED) {
        this.PROTECTED = PROTECTED;
    }


}