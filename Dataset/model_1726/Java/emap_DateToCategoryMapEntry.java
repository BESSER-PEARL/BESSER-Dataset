





import java.util.List;
import java.util.ArrayList;

public class emap_DateToCategoryMapEntry  {

    private String value;
    private String key;





    private emap_Book emap_book;


    public emap_DateToCategoryMapEntry(
        String value,        String key    ) {
        this.value = value;
        this.key = key;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public emap_Book getEmap_book() {
        return emap_book;
    }

    public void setEmap_book(emap_Book emap_book) {
        this.emap_book = emap_book;
    }

}