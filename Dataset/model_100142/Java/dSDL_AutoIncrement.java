





import java.util.List;
import java.util.ArrayList;

public class dSDL_AutoIncrement extends Property {

    private boolean autoIncrement;



    public dSDL_AutoIncrement(
        boolean autoIncrement    ) {
        super(
        );
        this.autoIncrement = autoIncrement;
    }


    public boolean getAutoincrement() {
        return autoIncrement;
    }

    public void setAutoincrement(boolean autoIncrement) {
        this.autoIncrement = autoIncrement;
    }


}