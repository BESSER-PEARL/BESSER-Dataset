





import java.util.List;
import java.util.ArrayList;

public class build_properties_Format extends IFunction {

    private String formatString;



    public build_properties_Format(
        String formatString    ) {
        super(
        );
        this.formatString = formatString;
    }


    public String getFormatstring() {
        return formatString;
    }

    public void setFormatstring(String formatString) {
        this.formatString = formatString;
    }


}