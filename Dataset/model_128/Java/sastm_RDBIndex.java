





import java.util.List;
import java.util.ArrayList;

public class sastm_RDBIndex extends OtherSyntaxObject {

    private boolean NotNull;
    private boolean IsUnique;



    public sastm_RDBIndex(
        boolean NotNull,        boolean IsUnique    ) {
        super(
        );
        this.NotNull = NotNull;
        this.IsUnique = IsUnique;
    }


    public boolean getNotnull() {
        return NotNull;
    }

    public void setNotnull(boolean NotNull) {
        this.NotNull = NotNull;
    }
    public boolean getIsunique() {
        return IsUnique;
    }

    public void setIsunique(boolean IsUnique) {
        this.IsUnique = IsUnique;
    }


}