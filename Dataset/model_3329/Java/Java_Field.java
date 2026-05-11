





import java.util.List;
import java.util.ArrayList;

public class Java_Field  {

    private boolean isPublic;
    private boolean isPrivate;
    private boolean isProtected;
    private String name;
    private boolean isStatic;





    private Type type;




    private Class class;


    public Java_Field(
        boolean isPublic,        boolean isPrivate,        boolean isProtected,        String name,        boolean isStatic    ) {
        this.isPublic = isPublic;
        this.isPrivate = isPrivate;
        this.isProtected = isProtected;
        this.name = name;
        this.isStatic = isStatic;
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
    public boolean getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(boolean isStatic) {
        this.isStatic = isStatic;
    }

    public Type getType() {
        return type;
    }

    public void setType(Type type) {
        this.type = type;
    }
    public Class getClass() {
        return class;
    }

    public void setClass(Class class) {
        this.class = class;
    }

}