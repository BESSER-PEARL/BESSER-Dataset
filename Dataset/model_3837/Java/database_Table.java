





import java.util.List;
import java.util.ArrayList;

public class database_Table  {

    private boolean is_local;
    private String name;



    public database_Table(
        boolean is_local,        String name    ) {
        this.is_local = is_local;
        this.name = name;
    }


    public boolean getIs_local() {
        return is_local;
    }

    public void setIs_local(boolean is_local) {
        this.is_local = is_local;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}