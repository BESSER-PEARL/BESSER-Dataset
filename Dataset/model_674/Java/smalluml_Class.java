





import java.util.List;
import java.util.ArrayList;

public class smalluml_Class extends Type {






    private List<smalluml_Class> smalluml_classs;


    public smalluml_Class(
    ) {
        super(
        );
        this.smalluml_classs = new ArrayList<>();
    }

    public smalluml_Class(
        ArrayList<smalluml_Class> smalluml_classs    ) {
        this.smalluml_classs = smalluml_classs;
    }


    public List<smalluml_Class> getSmalluml_classs() {
        return smalluml_classs;
    }

    public void addSmalluml_class(Smalluml_class smalluml_class) {
        this.smalluml_classs.add(smalluml_class);
    }

}