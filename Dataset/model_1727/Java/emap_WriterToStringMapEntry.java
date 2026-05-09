





import java.util.List;
import java.util.ArrayList;

public class emap_WriterToStringMapEntry  {

    private String value;





    private emap_Book emap_book;


    public emap_WriterToStringMapEntry(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public emap_Book getEmap_book() {
        return emap_book;
    }

    public void setEmap_book(emap_Book emap_book) {
        this.emap_book = emap_book;
    }

}