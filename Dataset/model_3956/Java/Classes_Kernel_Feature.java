





import java.util.List;
import java.util.ArrayList;

public class Classes_Kernel_Feature extends RedefinableElement {

    private boolean isStatic;



    public Classes_Kernel_Feature(
        boolean isStatic    ) {
        super(
        );
        this.isStatic = isStatic;
    }


    public boolean getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(boolean isStatic) {
        this.isStatic = isStatic;
    }


}