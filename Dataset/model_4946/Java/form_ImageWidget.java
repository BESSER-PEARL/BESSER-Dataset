





import java.util.List;
import java.util.ArrayList;

public class form_ImageWidget extends Duplicable, Widget {

    private boolean isADocument;





    private form_Expression form_expression;


    public form_ImageWidget(
        boolean isADocument    ) {
        super(
        );
        this.isADocument = isADocument;
    }


    public boolean getIsadocument() {
        return isADocument;
    }

    public void setIsadocument(boolean isADocument) {
        this.isADocument = isADocument;
    }

    public form_Expression getForm_expression() {
        return form_expression;
    }

    public void setForm_expression(form_Expression form_expression) {
        this.form_expression = form_expression;
    }

}