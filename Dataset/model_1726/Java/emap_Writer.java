





import java.util.List;
import java.util.ArrayList;

public class emap_Writer  {

    private String name;





    private emap_StringToWriterMapEntry emap_stringtowritermapentry;




    private emap_WriterToStringMapEntry emap_writertostringmapentry;


    public emap_Writer(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public emap_StringToWriterMapEntry getEmap_stringtowritermapentry() {
        return emap_stringtowritermapentry;
    }

    public void setEmap_stringtowritermapentry(emap_StringToWriterMapEntry emap_stringtowritermapentry) {
        this.emap_stringtowritermapentry = emap_stringtowritermapentry;
    }
    public emap_WriterToStringMapEntry getEmap_writertostringmapentry() {
        return emap_writertostringmapentry;
    }

    public void setEmap_writertostringmapentry(emap_WriterToStringMapEntry emap_writertostringmapentry) {
        this.emap_writertostringmapentry = emap_writertostringmapentry;
    }

}