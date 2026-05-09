





import java.util.List;
import java.util.ArrayList;

public class smalluml_Root  {






    private List<smalluml_Class> smalluml_classs;




    private List<smalluml_Type> smalluml_types;


    public smalluml_Root(
    ) {
        this.smalluml_classs = new ArrayList<>();
        this.smalluml_types = new ArrayList<>();
    }

    public smalluml_Root(
        ArrayList<smalluml_Class> smalluml_classs,        ArrayList<smalluml_Type> smalluml_types    ) {
        this.smalluml_classs = smalluml_classs;
        this.smalluml_types = smalluml_types;
    }


    public List<smalluml_Class> getSmalluml_classs() {
        return smalluml_classs;
    }

    public void addSmalluml_class(Smalluml_class smalluml_class) {
        this.smalluml_classs.add(smalluml_class);
    }
    public List<smalluml_Type> getSmalluml_types() {
        return smalluml_types;
    }

    public void addSmalluml_type(Smalluml_type smalluml_type) {
        this.smalluml_types.add(smalluml_type);
    }

}