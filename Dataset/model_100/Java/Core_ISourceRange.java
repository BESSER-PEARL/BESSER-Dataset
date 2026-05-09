





import java.util.List;
import java.util.ArrayList;

public class Core_ISourceRange  {

    private String length;
    private String offset;



    public Core_ISourceRange(
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


}