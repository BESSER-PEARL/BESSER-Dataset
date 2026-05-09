





import java.util.List;
import java.util.ArrayList;

public class sastm_RDBColumnDefinition extends Definition {

    private boolean NotNull;



    public sastm_RDBColumnDefinition(
        boolean NotNull    ) {
        super(
        );
        this.NotNull = NotNull;
    }


    public boolean getNotnull() {
        return NotNull;
    }

    public void setNotnull(boolean NotNull) {
        this.NotNull = NotNull;
    }


}