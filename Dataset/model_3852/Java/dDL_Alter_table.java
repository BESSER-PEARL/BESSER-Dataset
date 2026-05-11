





import java.util.List;
import java.util.ArrayList;

public class dDL_Alter_table extends Definition {

    private String id;
    private String add;
    private String enable;



    public dDL_Alter_table(
        String id,        String add,        String enable    ) {
        super(
        );
        this.id = id;
        this.add = add;
        this.enable = enable;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getAdd() {
        return add;
    }

    public void setAdd(String add) {
        this.add = add;
    }
    public String getEnable() {
        return enable;
    }

    public void setEnable(String enable) {
        this.enable = enable;
    }


}