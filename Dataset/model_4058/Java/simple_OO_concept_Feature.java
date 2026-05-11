





import java.util.List;
import java.util.ArrayList;

public class simple_OO_concept_Feature  {

    private boolean isProtected;
    private boolean isPrivate;
    private boolean isPublic;



    public simple_OO_concept_Feature(
        boolean isProtected,        boolean isPrivate,        boolean isPublic    ) {
        this.isProtected = isProtected;
        this.isPrivate = isPrivate;
        this.isPublic = isPublic;
    }


    public boolean getIsprotected() {
        return isProtected;
    }

    public void setIsprotected(boolean isProtected) {
        this.isProtected = isProtected;
    }
    public boolean getIsprivate() {
        return isPrivate;
    }

    public void setIsprivate(boolean isPrivate) {
        this.isPrivate = isPrivate;
    }
    public boolean getIspublic() {
        return isPublic;
    }

    public void setIspublic(boolean isPublic) {
        this.isPublic = isPublic;
    }


}