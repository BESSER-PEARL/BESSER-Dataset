





import java.util.List;
import java.util.ArrayList;

public class database_IndexElement extends DatabaseElement {

    private boolean asc;



    public database_IndexElement(
        boolean asc    ) {
        super(
        );
        this.asc = asc;
    }


    public boolean getAsc() {
        return asc;
    }

    public void setAsc(boolean asc) {
        this.asc = asc;
    }


}