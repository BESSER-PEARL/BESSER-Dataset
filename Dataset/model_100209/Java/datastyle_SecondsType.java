





import java.util.List;
import java.util.ArrayList;

public class datastyle_SecondsType  {

    private String decimalPlaces;
    private String style;





    private datastyle_DateStyleType datastyle_datestyletype;


    public datastyle_SecondsType(
        String decimalPlaces,        String style    ) {
        this.decimalPlaces = decimalPlaces;
        this.style = style;
    }


    public String getDecimalplaces() {
        return decimalPlaces;
    }

    public void setDecimalplaces(String decimalPlaces) {
        this.decimalPlaces = decimalPlaces;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }

    public datastyle_DateStyleType getDatastyle_datestyletype() {
        return datastyle_datestyletype;
    }

    public void setDatastyle_datestyletype(datastyle_DateStyleType datastyle_datestyletype) {
        this.datastyle_datestyletype = datastyle_datestyletype;
    }

}