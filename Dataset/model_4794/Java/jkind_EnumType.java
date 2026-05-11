





import java.util.List;
import java.util.ArrayList;

public class jkind_EnumType extends TypeDef {






    private List<jkind_EnumValue> jkind_enumvalues;


    public jkind_EnumType(
    ) {
        super(
        );
        this.jkind_enumvalues = new ArrayList<>();
    }

    public jkind_EnumType(
        ArrayList<jkind_EnumValue> jkind_enumvalues    ) {
        this.jkind_enumvalues = jkind_enumvalues;
    }


    public List<jkind_EnumValue> getJkind_enumvalues() {
        return jkind_enumvalues;
    }

    public void addJkind_enumvalue(Jkind_enumvalue jkind_enumvalue) {
        this.jkind_enumvalues.add(jkind_enumvalue);
    }

}