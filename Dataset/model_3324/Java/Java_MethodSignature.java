





import java.util.List;
import java.util.ArrayList;

public class Java_MethodSignature  {

    private boolean isProtected;
    private String name;
    private boolean isPublic;
    private boolean isPrivate;
    private boolean isStatic;



    public Java_MethodSignature(
        boolean isProtected,        String name,        boolean isPublic,        boolean isPrivate,        boolean isStatic    ) {
        this.isProtected = isProtected;
        this.name = name;
        this.isPublic = isPublic;
        this.isPrivate = isPrivate;
        this.isStatic = isStatic;
    }


    public boolean getIsprotected() {
        return isProtected;
    }

    public void setIsprotected(boolean isProtected) {
        this.isProtected = isProtected;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIspublic() {
        return isPublic;
    }

    public void setIspublic(boolean isPublic) {
        this.isPublic = isPublic;
    }
    public boolean getIsprivate() {
        return isPrivate;
    }

    public void setIsprivate(boolean isPrivate) {
        this.isPrivate = isPrivate;
    }
    public boolean getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(boolean isStatic) {
        this.isStatic = isStatic;
    }


}