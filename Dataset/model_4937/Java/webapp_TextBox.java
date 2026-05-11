





import java.util.List;
import java.util.ArrayList;

public class webapp_TextBox extends Control {

    private int maxLength;
    private String text;
    private boolean required;
    private int size;



    public webapp_TextBox(
        int maxLength,        String text,        boolean required,        int size    ) {
        super(
        );
        this.maxLength = maxLength;
        this.text = text;
        this.required = required;
        this.size = size;
    }


    public int getMaxlength() {
        return maxLength;
    }

    public void setMaxlength(int maxLength) {
        this.maxLength = maxLength;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public boolean getRequired() {
        return required;
    }

    public void setRequired(boolean required) {
        this.required = required;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }


}