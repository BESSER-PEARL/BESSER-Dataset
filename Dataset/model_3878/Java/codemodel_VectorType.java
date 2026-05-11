





import java.util.List;
import java.util.ArrayList;

public class codemodel_VectorType extends DataType {

    private String size;



    public codemodel_VectorType(
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


}