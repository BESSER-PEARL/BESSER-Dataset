





import java.util.List;
import java.util.ArrayList;

public class ccore_RuntimeItem extends Item {

    private String className;
    private boolean extendsClass;



    public ccore_RuntimeItem(
        String className,        boolean extendsClass    ) {
        super(
        );
        this.className = className;
        this.extendsClass = extendsClass;
    }


    public String getClassname() {
        return className;
    }

    public void setClassname(String className) {
        this.className = className;
    }
    public boolean getExtendsclass() {
        return extendsClass;
    }

    public void setExtendsclass(boolean extendsClass) {
        this.extendsClass = extendsClass;
    }


}