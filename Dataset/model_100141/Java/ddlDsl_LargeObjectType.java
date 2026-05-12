





import java.util.List;
import java.util.ArrayList;

public class ddlDsl_LargeObjectType extends SqlDataType {

    private int size;



    public ddlDsl_LargeObjectType(
        int size    ) {
        super(
        );
        this.size = size;
    }


    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }


}