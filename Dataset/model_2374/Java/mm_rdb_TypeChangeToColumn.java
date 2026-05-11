





import java.util.List;
import java.util.ArrayList;

public class mm_rdb_TypeChangeToColumn extends Operation {

    private String newType;



    public mm_rdb_TypeChangeToColumn(
        String newType    ) {
        super(
        );
        this.newType = newType;
    }


    public String getNewtype() {
        return newType;
    }

    public void setNewtype(String newType) {
        this.newType = newType;
    }


}