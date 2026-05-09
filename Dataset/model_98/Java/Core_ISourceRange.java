





import java.util.List;
import java.util.ArrayList;

public class Core_ISourceRange  {

    private String offset;
    private String length;



    public Core_ISourceRange(
        String offset,        String length    ) {
        this.offset = offset;
        this.length = length;
    }


    public String getOffset() {
        return offset;
    }

    public void setOffset(String offset) {
        this.offset = offset;
    }
    public String getLength() {
        return length;
    }

    public void setLength(String length) {
        this.length = length;
    }


}