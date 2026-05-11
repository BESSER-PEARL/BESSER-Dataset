





import java.util.List;
import java.util.ArrayList;

public class myDsl01_UIElement  {

    private String name;





    private myDsl01_EntryWindow mydsl01_entrywindow;


    public myDsl01_UIElement(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl01_EntryWindow getMydsl01_entrywindow() {
        return mydsl01_entrywindow;
    }

    public void setMydsl01_entrywindow(myDsl01_EntryWindow mydsl01_entrywindow) {
        this.mydsl01_entrywindow = mydsl01_entrywindow;
    }

}