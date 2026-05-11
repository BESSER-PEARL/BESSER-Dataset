





import java.util.List;
import java.util.ArrayList;

public class aadl2_ArrayableElement extends Element {






    private List<aadl2_ArrayDimension> aadl2_arraydimensions;


    public aadl2_ArrayableElement(
    ) {
        super(
        );
        this.aadl2_arraydimensions = new ArrayList<>();
    }

    public aadl2_ArrayableElement(
        ArrayList<aadl2_ArrayDimension> aadl2_arraydimensions    ) {
        this.aadl2_arraydimensions = aadl2_arraydimensions;
    }


    public List<aadl2_ArrayDimension> getAadl2_arraydimensions() {
        return aadl2_arraydimensions;
    }

    public void addAadl2_arraydimension(Aadl2_arraydimension aadl2_arraydimension) {
        this.aadl2_arraydimensions.add(aadl2_arraydimension);
    }

}