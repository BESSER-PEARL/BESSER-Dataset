





import java.util.List;
import java.util.ArrayList;

public class mapkey_Writer  {

    private String name;





    private mapkey_StringToWriterMapEntry mapkey_stringtowritermapentry;


    public mapkey_Writer(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mapkey_StringToWriterMapEntry getMapkey_stringtowritermapentry() {
        return mapkey_stringtowritermapentry;
    }

    public void setMapkey_stringtowritermapentry(mapkey_StringToWriterMapEntry mapkey_stringtowritermapentry) {
        this.mapkey_stringtowritermapentry = mapkey_stringtowritermapentry;
    }

}