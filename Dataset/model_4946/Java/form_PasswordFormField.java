





import java.util.List;
import java.util.ArrayList;

public class form_PasswordFormField extends SingleValuatedFormField {

    private int maxLength;



    public form_PasswordFormField(
        int maxLength    ) {
        super(
        );
        this.maxLength = maxLength;
    }


    public int getMaxlength() {
        return maxLength;
    }

    public void setMaxlength(int maxLength) {
        this.maxLength = maxLength;
    }


}