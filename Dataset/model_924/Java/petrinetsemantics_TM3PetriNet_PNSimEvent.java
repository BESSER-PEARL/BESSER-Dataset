





import java.util.List;
import java.util.ArrayList;

public class petrinetsemantics_TM3PetriNet_PNSimEvent  {

    private boolean internal;
    private int date;
    private String name;



    public petrinetsemantics_TM3PetriNet_PNSimEvent(
        boolean internal,        int date,        String name    ) {
        this.internal = internal;
        this.date = date;
        this.name = name;
    }


    public boolean getInternal() {
        return internal;
    }

    public void setInternal(boolean internal) {
        this.internal = internal;
    }
    public int getDate() {
        return date;
    }

    public void setDate(int date) {
        this.date = date;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}