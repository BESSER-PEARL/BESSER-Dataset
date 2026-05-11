





import java.util.List;
import java.util.ArrayList;

public class textlink_Region  {

    private String length;
    private String offset;





    private textlink_TextLocation textlink_textlocation;


    public textlink_Region(
        String length,        String offset    ) {
        this.length = length;
        this.offset = offset;
    }


    public String getLength() {
        return length;
    }

    public void setLength(String length) {
        this.length = length;
    }
    public String getOffset() {
        return offset;
    }

    public void setOffset(String offset) {
        this.offset = offset;
    }

    public textlink_TextLocation getTextlink_textlocation() {
        return textlink_textlocation;
    }

    public void setTextlink_textlocation(textlink_TextLocation textlink_textlocation) {
        this.textlink_textlocation = textlink_textlocation;
    }

}