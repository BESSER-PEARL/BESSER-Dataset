





import java.util.List;
import java.util.ArrayList;

public class henshin_text_Rollback extends SequentialProperties {

    private boolean rollback;



    public henshin_text_Rollback(
        boolean rollback    ) {
        super(
        );
        this.rollback = rollback;
    }


    public boolean getRollback() {
        return rollback;
    }

    public void setRollback(boolean rollback) {
        this.rollback = rollback;
    }


}