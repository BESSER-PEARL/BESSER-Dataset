





import java.util.List;
import java.util.ArrayList;

public class emapsample_WriterToNameMapEntry  {

    private String value;





    private emapsample_Writer emapsample_writer;




    private emapsample_BookStore emapsample_bookstore;


    public emapsample_WriterToNameMapEntry(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public emapsample_Writer getEmapsample_writer() {
        return emapsample_writer;
    }

    public void setEmapsample_writer(emapsample_Writer emapsample_writer) {
        this.emapsample_writer = emapsample_writer;
    }
    public emapsample_BookStore getEmapsample_bookstore() {
        return emapsample_bookstore;
    }

    public void setEmapsample_bookstore(emapsample_BookStore emapsample_bookstore) {
        this.emapsample_bookstore = emapsample_bookstore;
    }

}