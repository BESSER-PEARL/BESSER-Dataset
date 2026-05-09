





import java.util.List;
import java.util.ArrayList;

public class basic_TypeItem  {

    private int sourceEnd;
    private String typeName;
    private int sourceStart;



    public basic_TypeItem(
        int sourceEnd,        String typeName,        int sourceStart    ) {
        this.sourceEnd = sourceEnd;
        this.typeName = typeName;
        this.sourceStart = sourceStart;
    }


    public int getSourceend() {
        return sourceEnd;
    }

    public void setSourceend(int sourceEnd) {
        this.sourceEnd = sourceEnd;
    }
    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }
    public int getSourcestart() {
        return sourceStart;
    }

    public void setSourcestart(int sourceStart) {
        this.sourceStart = sourceStart;
    }


}