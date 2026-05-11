





import java.util.List;
import java.util.ArrayList;

public class aadl2_ArraySize extends Element {

    private String size;





    private aadl2_ArrayDimension aadl2_arraydimension;


    public aadl2_ArraySize(
        String size    ) {
        super(
        );
        this.size = size;
    }


    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }

    public aadl2_ArrayDimension getAadl2_arraydimension() {
        return aadl2_arraydimension;
    }

    public void setAadl2_arraydimension(aadl2_ArrayDimension aadl2_arraydimension) {
        this.aadl2_arraydimension = aadl2_arraydimension;
    }

}