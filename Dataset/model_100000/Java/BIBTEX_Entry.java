





import java.util.List;
import java.util.ArrayList;

public class BIBTEX_Entry extends LocatedElement {

    private String key;





    private List<Field> fields;


    public BIBTEX_Entry(
        String key    ) {
        super(
        );
        this.key = key;
        this.fields = new ArrayList<>();
    }

    public BIBTEX_Entry(
        String key        ArrayList<Field> fields    ) {
        this.key = key;
        this.fields = fields;
    }

    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public List<Field> getFields() {
        return fields;
    }

    public void addField(Field field) {
        this.fields.add(field);
    }

}