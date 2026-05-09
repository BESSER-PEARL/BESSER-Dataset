





import java.util.List;
import java.util.ArrayList;

public class Java5_ArrayType extends OrphanType {

    private String originalName;
    private int dimensions;



    public Java5_ArrayType(
        String originalName,        int dimensions    ) {
        super(
        );
        this.originalName = originalName;
        this.dimensions = dimensions;
    }


    public String getOriginalname() {
        return originalName;
    }

    public void setOriginalname(String originalName) {
        this.originalName = originalName;
    }
    public int getDimensions() {
        return dimensions;
    }

    public void setDimensions(int dimensions) {
        this.dimensions = dimensions;
    }


}