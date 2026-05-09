





import java.util.List;
import java.util.ArrayList;

public class hbmapkeys_StringToWriterMapEntry  {

    private String key;





    private hbmapkeys_Writer hbmapkeys_writer;




    private hbmapkeys_Book hbmapkeys_book;


    public hbmapkeys_StringToWriterMapEntry(
        String key    ) {
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public hbmapkeys_Writer getHbmapkeys_writer() {
        return hbmapkeys_writer;
    }

    public void setHbmapkeys_writer(hbmapkeys_Writer hbmapkeys_writer) {
        this.hbmapkeys_writer = hbmapkeys_writer;
    }
    public hbmapkeys_Book getHbmapkeys_book() {
        return hbmapkeys_book;
    }

    public void setHbmapkeys_book(hbmapkeys_Book hbmapkeys_book) {
        this.hbmapkeys_book = hbmapkeys_book;
    }

}