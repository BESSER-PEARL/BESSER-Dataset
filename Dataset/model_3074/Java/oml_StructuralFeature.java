





import java.util.List;
import java.util.ArrayList;

public class oml_StructuralFeature extends Feature {

    private String isMany;



    public oml_StructuralFeature(
        String isMany    ) {
        super(
        );
        this.isMany = isMany;
    }


    public String getIsmany() {
        return isMany;
    }

    public void setIsmany(String isMany) {
        this.isMany = isMany;
    }


}