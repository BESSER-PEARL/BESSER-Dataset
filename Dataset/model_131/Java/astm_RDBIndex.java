





import java.util.List;
import java.util.ArrayList;

public class astm_RDBIndex extends OtherSyntaxObject {

    private boolean IsUnique;
    private boolean NotNull;



    public astm_RDBIndex(
        boolean IsUnique,        boolean NotNull    ) {
        super(
        );
        this.IsUnique = IsUnique;
        this.NotNull = NotNull;
    }


    public boolean getIsunique() {
        return IsUnique;
    }

    public void setIsunique(boolean IsUnique) {
        this.IsUnique = IsUnique;
    }
    public boolean getNotnull() {
        return NotNull;
    }

    public void setNotnull(boolean NotNull) {
        this.NotNull = NotNull;
    }


}