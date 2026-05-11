





import java.util.List;
import java.util.ArrayList;

public class myDsl_enum_specifier  {

    private String enumt;
    private String identifier;





    private myDsl_type_specifier mydsl_type_specifier;


    public myDsl_enum_specifier(
        String enumt,        String identifier    ) {
        this.enumt = enumt;
        this.identifier = identifier;
    }


    public String getEnumt() {
        return enumt;
    }

    public void setEnumt(String enumt) {
        this.enumt = enumt;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public myDsl_type_specifier getMydsl_type_specifier() {
        return mydsl_type_specifier;
    }

    public void setMydsl_type_specifier(myDsl_type_specifier mydsl_type_specifier) {
        this.mydsl_type_specifier = mydsl_type_specifier;
    }

}