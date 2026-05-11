





import java.util.List;
import java.util.ArrayList;

public class jkind_RecordType extends TypeDef {






    private List<jkind_Field> jkind_fields;




    private List<jkind_Type> jkind_types;




    private jkind_RecordExpr jkind_recordexpr;


    public jkind_RecordType(
    ) {
        super(
        );
        this.jkind_fields = new ArrayList<>();
        this.jkind_types = new ArrayList<>();
    }

    public jkind_RecordType(
        ArrayList<jkind_Field> jkind_fields,        ArrayList<jkind_Type> jkind_types    ) {
        this.jkind_fields = jkind_fields;
        this.jkind_types = jkind_types;
    }


    public List<jkind_Field> getJkind_fields() {
        return jkind_fields;
    }

    public void addJkind_field(Jkind_field jkind_field) {
        this.jkind_fields.add(jkind_field);
    }
    public List<jkind_Type> getJkind_types() {
        return jkind_types;
    }

    public void addJkind_type(Jkind_type jkind_type) {
        this.jkind_types.add(jkind_type);
    }
    public jkind_RecordExpr getJkind_recordexpr() {
        return jkind_recordexpr;
    }

    public void setJkind_recordexpr(jkind_RecordExpr jkind_recordexpr) {
        this.jkind_recordexpr = jkind_recordexpr;
    }

}