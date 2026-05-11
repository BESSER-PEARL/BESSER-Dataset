





import java.util.List;
import java.util.ArrayList;

public class persistence_UrlAttribute extends Attribute {

    private String displayValue;



    public persistence_UrlAttribute(
        String displayValue    ) {
        super(
        );
        this.displayValue = displayValue;
    }


    public String getDisplayvalue() {
        return displayValue;
    }

    public void setDisplayvalue(String displayValue) {
        this.displayValue = displayValue;
    }


}