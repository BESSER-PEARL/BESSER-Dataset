





import java.util.List;
import java.util.ArrayList;

public class frameweb_DateTimeAttribute extends DomainAttribute {

    private String dateTimePrecision;



    public frameweb_DateTimeAttribute(
        String dateTimePrecision    ) {
        super(
        );
        this.dateTimePrecision = dateTimePrecision;
    }


    public String getDatetimeprecision() {
        return dateTimePrecision;
    }

    public void setDatetimeprecision(String dateTimePrecision) {
        this.dateTimePrecision = dateTimePrecision;
    }


}