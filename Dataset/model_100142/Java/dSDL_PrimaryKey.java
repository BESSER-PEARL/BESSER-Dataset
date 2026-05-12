





import java.util.List;
import java.util.ArrayList;

public class dSDL_PrimaryKey extends Property {

    private boolean primaryKey;



    public dSDL_PrimaryKey(
        boolean primaryKey    ) {
        super(
        );
        this.primaryKey = primaryKey;
    }


    public boolean getPrimarykey() {
        return primaryKey;
    }

    public void setPrimarykey(boolean primaryKey) {
        this.primaryKey = primaryKey;
    }


}