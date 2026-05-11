





import java.util.List;
import java.util.ArrayList;

public class core_actionstep_DBQueryParamId  {

    private String id;
    private int index;



    public core_actionstep_DBQueryParamId(
        String id,        int index    ) {
        this.id = id;
        this.index = index;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public int getIndex() {
        return index;
    }

    public void setIndex(int index) {
        this.index = index;
    }


}