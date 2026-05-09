





import java.util.List;
import java.util.ArrayList;

public class webapp_Tag extends Instruction {

    private String _property;





    private webapp_Form webapp_form;




    private webapp_Td webapp_td;


    public webapp_Tag(
        String _property    ) {
        super(
        );
        this._property = _property;
    }


    public String get_property() {
        return _property;
    }

    public void set_property(String _property) {
        this._property = _property;
    }

    public webapp_Form getWebapp_form() {
        return webapp_form;
    }

    public void setWebapp_form(webapp_Form webapp_form) {
        this.webapp_form = webapp_form;
    }
    public webapp_Td getWebapp_td() {
        return webapp_td;
    }

    public void setWebapp_td(webapp_Td webapp_td) {
        this.webapp_td = webapp_td;
    }

}