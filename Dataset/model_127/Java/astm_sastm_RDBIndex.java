





import java.util.List;
import java.util.ArrayList;

public class astm_sastm_RDBIndex extends OtherSyntaxObject {

    private boolean IsUnique;
    private boolean NotNull;





    private List<Name> names;


    public astm_sastm_RDBIndex(
        boolean IsUnique,        boolean NotNull    ) {
        super(
        );
        this.IsUnique = IsUnique;
        this.NotNull = NotNull;
        this.names = new ArrayList<>();
    }

    public astm_sastm_RDBIndex(
        boolean IsUnique,        boolean NotNull        ArrayList<Name> names    ) {
        this.IsUnique = IsUnique;
        this.NotNull = NotNull;
        this.names = names;
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

    public List<Name> getNames() {
        return names;
    }

    public void addName(Name name) {
        this.names.add(name);
    }

}