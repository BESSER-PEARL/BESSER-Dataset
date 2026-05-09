





import java.util.List;
import java.util.ArrayList;

public class javasimplified_Modifier  {

    private boolean isVolatile;
    private boolean isSynchronized;
    private boolean isFinal;
    private boolean isStatic;
    private String visibility;





    private javasimplified_Method javasimplified_method;




    private javasimplified_Class javasimplified_class;


    public javasimplified_Modifier(
        boolean isVolatile,        boolean isSynchronized,        boolean isFinal,        boolean isStatic,        String visibility    ) {
        this.isVolatile = isVolatile;
        this.isSynchronized = isSynchronized;
        this.isFinal = isFinal;
        this.isStatic = isStatic;
        this.visibility = visibility;
    }


    public boolean getIsvolatile() {
        return isVolatile;
    }

    public void setIsvolatile(boolean isVolatile) {
        this.isVolatile = isVolatile;
    }
    public boolean getIssynchronized() {
        return isSynchronized;
    }

    public void setIssynchronized(boolean isSynchronized) {
        this.isSynchronized = isSynchronized;
    }
    public boolean getIsfinal() {
        return isFinal;
    }

    public void setIsfinal(boolean isFinal) {
        this.isFinal = isFinal;
    }
    public boolean getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(boolean isStatic) {
        this.isStatic = isStatic;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }

    public javasimplified_Method getJavasimplified_method() {
        return javasimplified_method;
    }

    public void setJavasimplified_method(javasimplified_Method javasimplified_method) {
        this.javasimplified_method = javasimplified_method;
    }
    public javasimplified_Class getJavasimplified_class() {
        return javasimplified_class;
    }

    public void setJavasimplified_class(javasimplified_Class javasimplified_class) {
        this.javasimplified_class = javasimplified_class;
    }

}