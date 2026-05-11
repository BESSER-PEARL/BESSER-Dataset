





import java.util.List;
import java.util.ArrayList;

public class emfdb_A  {

    private float primitiveValues;
    private String string;
    private String strings;
    private float notUniqueValues;





    private List<emfdb_B> emfdb_bs;




    private List<emfdb_C> emfdb_cs;


    public emfdb_A(
        float primitiveValues,        String string,        String strings,        float notUniqueValues    ) {
        this.primitiveValues = primitiveValues;
        this.string = string;
        this.strings = strings;
        this.notUniqueValues = notUniqueValues;
        this.emfdb_bs = new ArrayList<>();
        this.emfdb_cs = new ArrayList<>();
    }

    public emfdb_A(
        float primitiveValues,        String string,        String strings,        float notUniqueValues        ArrayList<emfdb_B> emfdb_bs,        ArrayList<emfdb_C> emfdb_cs    ) {
        this.primitiveValues = primitiveValues;
        this.string = string;
        this.strings = strings;
        this.notUniqueValues = notUniqueValues;
        this.emfdb_bs = emfdb_bs;
        this.emfdb_cs = emfdb_cs;
    }

    public float getPrimitivevalues() {
        return primitiveValues;
    }

    public void setPrimitivevalues(float primitiveValues) {
        this.primitiveValues = primitiveValues;
    }
    public String getString() {
        return string;
    }

    public void setString(String string) {
        this.string = string;
    }
    public String getStrings() {
        return strings;
    }

    public void setStrings(String strings) {
        this.strings = strings;
    }
    public float getNotuniquevalues() {
        return notUniqueValues;
    }

    public void setNotuniquevalues(float notUniqueValues) {
        this.notUniqueValues = notUniqueValues;
    }

    public List<emfdb_B> getEmfdb_bs() {
        return emfdb_bs;
    }

    public void addEmfdb_b(Emfdb_b emfdb_b) {
        this.emfdb_bs.add(emfdb_b);
    }
    public List<emfdb_C> getEmfdb_cs() {
        return emfdb_cs;
    }

    public void addEmfdb_c(Emfdb_c emfdb_c) {
        this.emfdb_cs.add(emfdb_c);
    }

}