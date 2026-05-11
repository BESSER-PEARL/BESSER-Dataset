





import java.util.List;
import java.util.ArrayList;

public class iot2_Expression_TableConstructor extends Expression {






    private List<iot2_Field> iot2_fields;


    public iot2_Expression_TableConstructor(
    ) {
        super(
        );
        this.iot2_fields = new ArrayList<>();
    }

    public iot2_Expression_TableConstructor(
        ArrayList<iot2_Field> iot2_fields    ) {
        this.iot2_fields = iot2_fields;
    }


    public List<iot2_Field> getIot2_fields() {
        return iot2_fields;
    }

    public void addIot2_field(Iot2_field iot2_field) {
        this.iot2_fields.add(iot2_field);
    }

}