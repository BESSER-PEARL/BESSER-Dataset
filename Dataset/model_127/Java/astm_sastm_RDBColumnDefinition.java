





import java.util.List;
import java.util.ArrayList;

public class astm_sastm_RDBColumnDefinition extends Definition {

    private boolean NotNull;





    private Name name;


    public astm_sastm_RDBColumnDefinition(
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

    public Name getName() {
        return name;
    }

    public void setName(Name name) {
        this.name = name;
    }

}