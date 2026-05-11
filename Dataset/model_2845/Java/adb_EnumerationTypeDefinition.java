





import java.util.List;
import java.util.ArrayList;

public class adb_EnumerationTypeDefinition extends TypeDefinition {

    private String enumerationliteralspecifications;



    public adb_EnumerationTypeDefinition(
        String enumerationliteralspecifications    ) {
        super(
        );
        this.enumerationliteralspecifications = enumerationliteralspecifications;
    }


    public String getEnumerationliteralspecifications() {
        return enumerationliteralspecifications;
    }

    public void setEnumerationliteralspecifications(String enumerationliteralspecifications) {
        this.enumerationliteralspecifications = enumerationliteralspecifications;
    }


}