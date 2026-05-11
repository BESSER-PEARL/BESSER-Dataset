





import java.util.List;
import java.util.ArrayList;

public class form_TextAreaFormField extends SingleValuatedFormField {

    private int maxHeigth;
    private int maxLength;



    public form_TextAreaFormField(
        int maxHeigth,        int maxLength    ) {
        super(
        );
        this.maxHeigth = maxHeigth;
        this.maxLength = maxLength;
    }


    public int getMaxheigth() {
        return maxHeigth;
    }

    public void setMaxheigth(int maxHeigth) {
        this.maxHeigth = maxHeigth;
    }
    public int getMaxlength() {
        return maxLength;
    }

    public void setMaxlength(int maxLength) {
        this.maxLength = maxLength;
    }


}