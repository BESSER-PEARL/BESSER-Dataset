





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_datatypes_CharacterSet extends SQLObject {

    private String encoding;
    private String repertoire;
    private String defaultCollation;



    public sqlmodel_datatypes_CharacterSet(
        String encoding,        String repertoire,        String defaultCollation    ) {
        super(
        );
        this.encoding = encoding;
        this.repertoire = repertoire;
        this.defaultCollation = defaultCollation;
    }


    public String getEncoding() {
        return encoding;
    }

    public void setEncoding(String encoding) {
        this.encoding = encoding;
    }
    public String getRepertoire() {
        return repertoire;
    }

    public void setRepertoire(String repertoire) {
        this.repertoire = repertoire;
    }
    public String getDefaultcollation() {
        return defaultCollation;
    }

    public void setDefaultcollation(String defaultCollation) {
        this.defaultCollation = defaultCollation;
    }


}