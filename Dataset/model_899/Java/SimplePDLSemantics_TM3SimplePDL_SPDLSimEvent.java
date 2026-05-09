





import java.util.List;
import java.util.ArrayList;

public class SimplePDLSemantics_TM3SimplePDL_SPDLSimEvent  {

    private String name;
    private int date;
    private boolean internal;



    public SimplePDLSemantics_TM3SimplePDL_SPDLSimEvent(
        String name,        int date,        boolean internal    ) {
        this.name = name;
        this.date = date;
        this.internal = internal;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getDate() {
        return date;
    }

    public void setDate(int date) {
        this.date = date;
    }
    public boolean getInternal() {
        return internal;
    }

    public void setInternal(boolean internal) {
        this.internal = internal;
    }


}