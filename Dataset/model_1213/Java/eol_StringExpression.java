





import java.util.List;
import java.util.ArrayList;

public class eol_StringExpression extends SummableExpression, ComparableExpression {

    private String value;





    private eol_IPackage eol_ipackage;


    public eol_StringExpression(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public eol_IPackage getEol_ipackage() {
        return eol_ipackage;
    }

    public void setEol_ipackage(eol_IPackage eol_ipackage) {
        this.eol_ipackage = eol_ipackage;
    }

}