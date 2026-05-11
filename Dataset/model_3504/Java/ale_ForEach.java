





import java.util.List;
import java.util.ArrayList;

public class ale_ForEach extends Statement {

    private String iterator;



    public ale_ForEach(
        String iterator    ) {
        super(
        );
        this.iterator = iterator;
    }


    public String getIterator() {
        return iterator;
    }

    public void setIterator(String iterator) {
        this.iterator = iterator;
    }


}