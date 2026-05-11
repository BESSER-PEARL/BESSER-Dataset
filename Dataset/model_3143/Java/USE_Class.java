





import java.util.List;
import java.util.ArrayList;

public class USE_Class  {

    private boolean abstract;
    private String name;





    private List<USE_Class> use_classs;


    public USE_Class(
        boolean abstract,        String name    ) {
        this.abstract = abstract;
        this.name = name;
        this.use_classs = new ArrayList<>();
    }

    public USE_Class(
        boolean abstract,        String name        ArrayList<USE_Class> use_classs    ) {
        this.abstract = abstract;
        this.name = name;
        this.use_classs = use_classs;
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

    public List<USE_Class> getUse_classs() {
        return use_classs;
    }

    public void addUse_class(Use_class use_class) {
        this.use_classs.add(use_class);
    }

}