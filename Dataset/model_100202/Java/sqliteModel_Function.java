





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_Function extends Expression, ConfigurationStatement {

    private boolean all;



    public sqliteModel_Function(
        boolean all    ) {
        super(
        );
        this.all = all;
    }


    public boolean getAll() {
        return all;
    }

    public void setAll(boolean all) {
        this.all = all;
    }


}