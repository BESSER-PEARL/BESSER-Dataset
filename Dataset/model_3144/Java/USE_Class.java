





import java.util.List;
import java.util.ArrayList;

public class USE_Class  {

    private boolean abstract;
    private String name;





    private USE_Class use_class;


    public USE_Class(
        boolean abstract,        String name    ) {
        this.abstract = abstract;
        this.name = name;
    }


    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public USE_Class getUse_class() {
        return use_class;
    }

    public void setUse_class(USE_Class use_class) {
        this.use_class = use_class;
    }

}