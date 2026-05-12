





import java.util.List;
import java.util.ArrayList;

public class petrinetsemantics_TM3PetriNet_PNSimEvent  {

    private String name;
    private boolean internal;
    private int date;



    public petrinetsemantics_TM3PetriNet_PNSimEvent(
        String name,        boolean internal,        int date    ) {
        this.name = name;
        this.internal = internal;
        this.date = date;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
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


}