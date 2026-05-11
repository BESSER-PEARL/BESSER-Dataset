





import java.util.List;
import java.util.ArrayList;

public class webApplication_content_MultipleContent extends Content {

    private int size;
    private boolean paginated;



    public webApplication_content_MultipleContent(
        int size,        boolean paginated    ) {
        super(
        );
        this.size = size;
        this.paginated = paginated;
    }


    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public boolean getPaginated() {
        return paginated;
    }

    public void setPaginated(boolean paginated) {
        this.paginated = paginated;
    }


}