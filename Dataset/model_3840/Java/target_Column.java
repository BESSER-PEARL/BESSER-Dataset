





import java.util.List;
import java.util.ArrayList;

public class target_Column  {

    private String type;
    private String name;





    private target_Table target_table;




    private target_FKey target_fkey;




    private target_Table target_table;


    public target_Column(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public target_Table getTarget_table() {
        return target_table;
    }

    public void setTarget_table(target_Table target_table) {
        this.target_table = target_table;
    }
    public target_FKey getTarget_fkey() {
        return target_fkey;
    }

    public void setTarget_fkey(target_FKey target_fkey) {
        this.target_fkey = target_fkey;
    }
    public target_Table getTarget_table() {
        return target_table;
    }

    public void setTarget_table(target_Table target_table) {
        this.target_table = target_table;
    }

}