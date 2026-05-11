





import java.util.List;
import java.util.ArrayList;

public class ddlDsl_SqlCharacter extends SqlDataType {

    private int size;
    private boolean national;



    public ddlDsl_SqlCharacter(
        int size,        boolean national    ) {
        super(
        );
        this.size = size;
        this.national = national;
    }


    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public boolean getNational() {
        return national;
    }

    public void setNational(boolean national) {
        this.national = national;
    }


}