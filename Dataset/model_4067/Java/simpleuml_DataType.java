





import java.util.List;
import java.util.ArrayList;

public class simpleuml_DataType extends Type {






    private simpleuml_Property simpleuml_property;




    private List<simpleuml_Property> simpleuml_propertys;


    public simpleuml_DataType(
    ) {
        super(
        );
        this.simpleuml_propertys = new ArrayList<>();
    }

    public simpleuml_DataType(
        ArrayList<simpleuml_Property> simpleuml_propertys    ) {
        this.simpleuml_propertys = simpleuml_propertys;
    }


    public simpleuml_Property getSimpleuml_property() {
        return simpleuml_property;
    }

    public void setSimpleuml_property(simpleuml_Property simpleuml_property) {
        this.simpleuml_property = simpleuml_property;
    }
    public List<simpleuml_Property> getSimpleuml_propertys() {
        return simpleuml_propertys;
    }

    public void addSimpleuml_property(Simpleuml_property simpleuml_property) {
        this.simpleuml_propertys.add(simpleuml_property);
    }

}