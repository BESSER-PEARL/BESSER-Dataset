





import java.util.List;
import java.util.ArrayList;

public class Java_Class extends ObjectType {

    private boolean isPublic;
    private boolean isStatic;



    public Java_Class(
        boolean isPublic,        boolean isStatic    ) {
        super(
        );
        this.isPublic = isPublic;
        this.isStatic = isStatic;
    }


    public boolean getIspublic() {
        return isPublic;
    }

    public void setIspublic(boolean isPublic) {
        this.isPublic = isPublic;
    }
    public boolean getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(boolean isStatic) {
        this.isStatic = isStatic;
    }


}