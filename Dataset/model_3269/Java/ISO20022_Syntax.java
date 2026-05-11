





import java.util.List;
import java.util.ArrayList;

public class ISO20022_Syntax extends ModelEntity {






    private List<ISO20022_Encoding> iso20022_encodings;




    private ISO20022_Encoding iso20022_encoding;


    public ISO20022_Syntax(
    ) {
        super(
        );
        this.iso20022_encodings = new ArrayList<>();
    }

    public ISO20022_Syntax(
        ArrayList<ISO20022_Encoding> iso20022_encodings    ) {
        this.iso20022_encodings = iso20022_encodings;
    }


    public List<ISO20022_Encoding> getIso20022_encodings() {
        return iso20022_encodings;
    }

    public void addIso20022_encoding(Iso20022_encoding iso20022_encoding) {
        this.iso20022_encodings.add(iso20022_encoding);
    }
    public ISO20022_Encoding getIso20022_encoding() {
        return iso20022_encoding;
    }

    public void setIso20022_encoding(ISO20022_Encoding iso20022_encoding) {
        this.iso20022_encoding = iso20022_encoding;
    }

}