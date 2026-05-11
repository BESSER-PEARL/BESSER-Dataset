





import java.util.List;
import java.util.ArrayList;

public class Java_MethodSignature  {

    private boolean isPrivate;
    private boolean isProtected;
    private boolean isStatic;
    private String name;
    private boolean isPublic;





    private Type type;


    public Java_MethodSignature(
        boolean isPrivate,        boolean isProtected,        boolean isStatic,        String name,        boolean isPublic    ) {
        this.isPrivate = isPrivate;
        this.isProtected = isProtected;
        this.isStatic = isStatic;
        this.name = name;
        this.isPublic = isPublic;
    }


    public boolean getIsprivate() {
        return isPrivate;
    }

    public void setIsprivate(boolean isPrivate) {
        this.isPrivate = isPrivate;
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

    public Type getType() {
        return type;
    }

    public void setType(Type type) {
        this.type = type;
    }

}