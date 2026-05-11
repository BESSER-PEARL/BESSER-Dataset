





import java.util.List;
import java.util.ArrayList;

public class dot_AttributedItem  {






    private List<dot_StringToStringMapEntry> dot_stringtostringmapentrys;


    public dot_AttributedItem(
    ) {
        this.dot_stringtostringmapentrys = new ArrayList<>();
    }

    public dot_AttributedItem(
        ArrayList<dot_StringToStringMapEntry> dot_stringtostringmapentrys    ) {
        this.dot_stringtostringmapentrys = dot_stringtostringmapentrys;
    }


    public List<dot_StringToStringMapEntry> getDot_stringtostringmapentrys() {
        return dot_stringtostringmapentrys;
    }

    public void addDot_stringtostringmapentry(Dot_stringtostringmapentry dot_stringtostringmapentry) {
        this.dot_stringtostringmapentrys.add(dot_stringtostringmapentry);
    }

}