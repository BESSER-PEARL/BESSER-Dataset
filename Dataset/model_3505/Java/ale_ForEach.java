





import java.util.List;
import java.util.ArrayList;

public class ale_ForEach extends Statement {

    private String iterator;





    private ale_Block ale_block;


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

    public ale_Block getAle_block() {
        return ale_block;
    }

    public void setAle_block(ale_Block ale_block) {
        this.ale_block = ale_block;
    }

}