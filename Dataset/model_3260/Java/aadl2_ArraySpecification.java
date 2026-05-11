





import java.util.List;
import java.util.ArrayList;

public class aadl2_ArraySpecification extends Element {

    private String dimension;





    private List<aadl2_ArraySize> aadl2_arraysizes;


    public aadl2_ArraySpecification(
        String dimension    ) {
        super(
        );
        this.dimension = dimension;
        this.aadl2_arraysizes = new ArrayList<>();
    }

    public aadl2_ArraySpecification(
        String dimension        ArrayList<aadl2_ArraySize> aadl2_arraysizes    ) {
        this.dimension = dimension;
        this.aadl2_arraysizes = aadl2_arraysizes;
    }

    public String getDimension() {
        return dimension;
    }

    public void setDimension(String dimension) {
        this.dimension = dimension;
    }

    public List<aadl2_ArraySize> getAadl2_arraysizes() {
        return aadl2_arraysizes;
    }

    public void addAadl2_arraysize(Aadl2_arraysize aadl2_arraysize) {
        this.aadl2_arraysizes.add(aadl2_arraysize);
    }

}