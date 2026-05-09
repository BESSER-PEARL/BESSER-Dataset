





import java.util.List;
import java.util.ArrayList;

public class ryz_Choice  {

    private String selected;
    private String value;
    private String text;





    private ryz_MultipleChoice ryz_multiplechoice;


    public ryz_Choice(
        String selected,        String value,        String text    ) {
        this.selected = selected;
        this.value = value;
        this.text = text;
    }


    public String getSelected() {
        return selected;
    }

    public void setSelected(String selected) {
        this.selected = selected;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public ryz_MultipleChoice getRyz_multiplechoice() {
        return ryz_multiplechoice;
    }

    public void setRyz_multiplechoice(ryz_MultipleChoice ryz_multiplechoice) {
        this.ryz_multiplechoice = ryz_multiplechoice;
    }

}