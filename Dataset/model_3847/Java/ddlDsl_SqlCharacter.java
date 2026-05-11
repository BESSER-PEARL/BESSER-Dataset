





import java.util.List;
import java.util.ArrayList;

public class ddlDsl_SqlCharacter extends SqlDataType {

    private boolean national;
    private int size;



    public ddlDsl_SqlCharacter(
        boolean national,        int size    ) {
        super(
        );
        this.national = national;
        this.size = size;
    }


    public boolean getNational() {
        return national;
    }

    public void setNational(boolean national) {
        this.national = national;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }


}