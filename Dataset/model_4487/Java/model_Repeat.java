





import java.util.List;
import java.util.ArrayList;

public class model_Repeat extends Command {

    private int count;





    private model_Block model_block;


    public model_Repeat(
        int count    ) {
        super(
        );
        this.count = count;
    }


    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
    }

    public model_Block getModel_block() {
        return model_block;
    }

    public void setModel_block(model_Block model_block) {
        this.model_block = model_block;
    }

}