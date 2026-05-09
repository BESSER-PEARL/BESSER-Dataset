





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Variantdef  {

    private String name;
    private boolean current;



    public eaglemodel_Variantdef(
        String name,        boolean current    ) {
        this.name = name;
        this.current = current;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getCurrent() {
        return current;
    }

    public void setCurrent(boolean current) {
        this.current = current;
    }


}