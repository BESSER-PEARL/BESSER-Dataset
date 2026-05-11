





import java.util.List;
import java.util.ArrayList;

public class MARTE_GRM_StorageResource extends Resource {

    private String elementSize;



    public MARTE_GRM_StorageResource(
        String elementSize    ) {
        super(
        );
        this.elementSize = elementSize;
    }


    public String getElementsize() {
        return elementSize;
    }

    public void setElementsize(String elementSize) {
        this.elementSize = elementSize;
    }


}