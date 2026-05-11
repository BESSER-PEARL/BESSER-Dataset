





import java.util.List;
import java.util.ArrayList;

public class SQL2003_V2_ARRAY extends CollectionType {

    private String num_elements;



    public SQL2003_V2_ARRAY(
        String num_elements    ) {
        super(
        );
        this.num_elements = num_elements;
    }


    public String getNum_elements() {
        return num_elements;
    }

    public void setNum_elements(String num_elements) {
        this.num_elements = num_elements;
    }


}