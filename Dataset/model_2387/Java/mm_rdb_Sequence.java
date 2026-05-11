





import java.util.List;
import java.util.ArrayList;

public class mm_rdb_Sequence  {

    private int startValue;
    private String name;



    public mm_rdb_Sequence(
        int startValue,        String name    ) {
        this.startValue = startValue;
        this.name = name;
    }


    public int getStartvalue() {
        return startValue;
    }

    public void setStartvalue(int startValue) {
        this.startValue = startValue;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}