





import java.util.List;
import java.util.ArrayList;

public class form_FormField extends Duplicable, Validable, Widget {

    private String exampleMessagePosition;
    private String description;





    private form_Expression form_expression;


    public form_FormField(
        String exampleMessagePosition,        String description    ) {
        super(
        );
        this.exampleMessagePosition = exampleMessagePosition;
        this.description = description;
    }


    public String getExamplemessageposition() {
        return exampleMessagePosition;
    }

    public void setExamplemessageposition(String exampleMessagePosition) {
        this.exampleMessagePosition = exampleMessagePosition;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public form_Expression getForm_expression() {
        return form_expression;
    }

    public void setForm_expression(form_Expression form_expression) {
        this.form_expression = form_expression;
    }

}