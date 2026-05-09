





import java.util.List;
import java.util.ArrayList;

public class hbmapkeys_City  {

    private String name;





    private hbmapkeys_WriterToCityMapEntry hbmapkeys_writertocitymapentry;




    private hbmapkeys_Writer hbmapkeys_writer;


    public hbmapkeys_City(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public hbmapkeys_WriterToCityMapEntry getHbmapkeys_writertocitymapentry() {
        return hbmapkeys_writertocitymapentry;
    }

    public void setHbmapkeys_writertocitymapentry(hbmapkeys_WriterToCityMapEntry hbmapkeys_writertocitymapentry) {
        this.hbmapkeys_writertocitymapentry = hbmapkeys_writertocitymapentry;
    }
    public hbmapkeys_Writer getHbmapkeys_writer() {
        return hbmapkeys_writer;
    }

    public void setHbmapkeys_writer(hbmapkeys_Writer hbmapkeys_writer) {
        this.hbmapkeys_writer = hbmapkeys_writer;
    }

}