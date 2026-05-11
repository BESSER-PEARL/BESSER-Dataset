





import java.util.List;
import java.util.ArrayList;

public class Java_Field  {

    private boolean isProtected;
    private boolean isStatic;
    private boolean isPrivate;
    private boolean isPublic;
    private String name;



    public Java_Field(
        boolean isProtected,        boolean isStatic,        boolean isPrivate,        boolean isPublic,        String name    ) {
        this.isProtected = isProtected;
        this.isStatic = isStatic;
        this.isPrivate = isPrivate;
        this.isPublic = isPublic;
        this.name = name;
    }


    public boolean getIsprotected() {
        return isProtected;
    }

    public void setIsprotected(boolean isProtected) {
        this.isProtected = isProtected;
    }
    public boolean getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(boolean isStatic) {
        this.isStatic = isStatic;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}