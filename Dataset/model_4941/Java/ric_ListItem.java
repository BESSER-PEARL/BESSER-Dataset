





import java.util.List;
import java.util.ArrayList;

public class ric_ListItem  {

    private String text;
    private String format;





    private ric_OrderedList ric_orderedlist;




    private ric_UnorderedList ric_unorderedlist;


    public ric_ListItem(
        String text,        String format    ) {
        this.text = text;
        this.format = format;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getFormat() {
        return format;
    }

    public void setFormat(String format) {
        this.format = format;
    }

    public ric_OrderedList getRic_orderedlist() {
        return ric_orderedlist;
    }

    public void setRic_orderedlist(ric_OrderedList ric_orderedlist) {
        this.ric_orderedlist = ric_orderedlist;
    }
    public ric_UnorderedList getRic_unorderedlist() {
        return ric_unorderedlist;
    }

    public void setRic_unorderedlist(ric_UnorderedList ric_unorderedlist) {
        this.ric_unorderedlist = ric_unorderedlist;
    }

}