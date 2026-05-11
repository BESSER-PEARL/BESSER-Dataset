





import java.util.List;
import java.util.ArrayList;

public class cmof_Feature extends RedefinableElement {

    private String isStatic;



    public cmof_Feature(
        String isStatic    ) {
        super(
        );
        this.isStatic = isStatic;
    }


    public String getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(String isStatic) {
        this.isStatic = isStatic;
    }


}