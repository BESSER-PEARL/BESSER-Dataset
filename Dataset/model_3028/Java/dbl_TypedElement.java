





import java.util.List;
import java.util.ArrayList;

public class dbl_TypedElement  {






    private List<dbl_ArrayDimension> dbl_arraydimensions;


    public dbl_TypedElement(
    ) {
        this.dbl_arraydimensions = new ArrayList<>();
    }

    public dbl_TypedElement(
        ArrayList<dbl_ArrayDimension> dbl_arraydimensions    ) {
        this.dbl_arraydimensions = dbl_arraydimensions;
    }


    public List<dbl_ArrayDimension> getDbl_arraydimensions() {
        return dbl_arraydimensions;
    }

    public void addDbl_arraydimension(Dbl_arraydimension dbl_arraydimension) {
        this.dbl_arraydimensions.add(dbl_arraydimension);
    }

}