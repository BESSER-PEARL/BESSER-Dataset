





import java.util.List;
import java.util.ArrayList;

public class Java_Class extends ObjectType {

    private boolean isStatic;
    private boolean isPublic;



    public Java_Class(
        boolean isStatic,        boolean isPublic    ) {
        super(
        );
        this.isStatic = isStatic;
        this.isPublic = isPublic;
    }


    public boolean getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(boolean isStatic) {
        this.isStatic = isStatic;
    }
    public boolean getIspublic() {
        return isPublic;
    }

    public void setIspublic(boolean isPublic) {
        this.isPublic = isPublic;
    }


}