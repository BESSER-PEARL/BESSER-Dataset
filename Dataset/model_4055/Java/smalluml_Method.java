





import java.util.List;
import java.util.ArrayList;

public class smalluml_Method extends NamedElement {






    private smalluml_Class smalluml_class;




    private List<smalluml_Type> smalluml_types;




    private smalluml_Type smalluml_type;


    public smalluml_Method(
    ) {
        super(
        );
        this.smalluml_types = new ArrayList<>();
    }

    public smalluml_Method(
        ArrayList<smalluml_Type> smalluml_types    ) {
        this.smalluml_types = smalluml_types;
    }


    public smalluml_Class getSmalluml_class() {
        return smalluml_class;
    }

    public void setSmalluml_class(smalluml_Class smalluml_class) {
        this.smalluml_class = smalluml_class;
    }
    public List<smalluml_Type> getSmalluml_types() {
        return smalluml_types;
    }

    public void addSmalluml_type(Smalluml_type smalluml_type) {
        this.smalluml_types.add(smalluml_type);
    }
    public smalluml_Type getSmalluml_type() {
        return smalluml_type;
    }

    public void setSmalluml_type(smalluml_Type smalluml_type) {
        this.smalluml_type = smalluml_type;
    }

}