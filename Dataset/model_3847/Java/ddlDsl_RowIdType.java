





import java.util.List;
import java.util.ArrayList;

public class ddlDsl_RowIdType extends SqlDataType {

    private int size;



    public ddlDsl_RowIdType(
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