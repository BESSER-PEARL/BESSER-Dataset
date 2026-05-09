





import java.util.List;
import java.util.ArrayList;

public class emapsample_StringToWriterMapEntry  {

    private String key;





    private emapsample_Writer emapsample_writer;




    private emapsample_Book emapsample_book;


    public emapsample_StringToWriterMapEntry(
        String key    ) {
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public emapsample_Writer getEmapsample_writer() {
        return emapsample_writer;
    }

    public void setEmapsample_writer(emapsample_Writer emapsample_writer) {
        this.emapsample_writer = emapsample_writer;
    }
    public emapsample_Book getEmapsample_book() {
        return emapsample_book;
    }

    public void setEmapsample_book(emapsample_Book emapsample_book) {
        this.emapsample_book = emapsample_book;
    }

}