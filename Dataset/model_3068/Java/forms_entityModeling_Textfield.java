





import java.util.List;
import java.util.ArrayList;

public class forms_entityModeling_Textfield extends AttributePageElement {

    private String allowedValueFormat;



    public forms_entityModeling_Textfield(
        String allowedValueFormat    ) {
        super(
        );
        this.allowedValueFormat = allowedValueFormat;
    }


    public String getAllowedvalueformat() {
        return allowedValueFormat;
    }

    public void setAllowedvalueformat(String allowedValueFormat) {
        this.allowedValueFormat = allowedValueFormat;
    }


}