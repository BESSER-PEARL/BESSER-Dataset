





import java.util.List;
import java.util.ArrayList;

public class form_DateFormField extends SingleValuatedFormField {

    private String displayFormat;
    private String initialFormat;



    public form_DateFormField(
        String displayFormat,        String initialFormat    ) {
        super(
        );
        this.displayFormat = displayFormat;
        this.initialFormat = initialFormat;
    }


    public String getDisplayformat() {
        return displayFormat;
    }

    public void setDisplayformat(String displayFormat) {
        this.displayFormat = displayFormat;
    }
    public String getInitialformat() {
        return initialFormat;
    }

    public void setInitialformat(String initialFormat) {
        this.initialFormat = initialFormat;
    }


}