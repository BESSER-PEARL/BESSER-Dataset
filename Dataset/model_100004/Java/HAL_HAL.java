





import java.util.List;
import java.util.ArrayList;

public class HAL_HAL  {






    private List<Entry> entrys;


    public HAL_HAL(
    ) {
        this.entrys = new ArrayList<>();
    }

    public HAL_HAL(
        ArrayList<Entry> entrys    ) {
        this.entrys = entrys;
    }


    public List<Entry> getEntrys() {
        return entrys;
    }

    public void addEntry(Entry entry) {
        this.entrys.add(entry);
    }

}