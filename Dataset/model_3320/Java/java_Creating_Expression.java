





import java.util.List;
import java.util.ArrayList;

public class java_Creating_Expression  {

    private String className;
    private String typeSpecifier;



    public java_Creating_Expression(
        String className,        String typeSpecifier    ) {
        this.className = className;
        this.typeSpecifier = typeSpecifier;
    }


    public String getClassname() {
        return className;
    }

    public void setClassname(String className) {
        this.className = className;
    }
    public String getTypespecifier() {
        return typeSpecifier;
    }

    public void setTypespecifier(String typeSpecifier) {
        this.typeSpecifier = typeSpecifier;
    }


}