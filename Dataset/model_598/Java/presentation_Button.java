





import java.util.List;
import java.util.ArrayList;

public class presentation_Button extends Control {

    private String alignment;
    private String text;
    private String group1;
    private String image;
    private String selection;
    private String grayed;



    public presentation_Button(
        String alignment,        String text,        String group1,        String image,        String selection,        String grayed    ) {
        super(
        );
        this.alignment = alignment;
        this.text = text;
        this.group1 = group1;
        this.image = image;
        this.selection = selection;
        this.grayed = grayed;
    }


    public String getAlignment() {
        return alignment;
    }

    public void setAlignment(String alignment) {
        this.alignment = alignment;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getGroup1() {
        return group1;
    }

    public void setGroup1(String group1) {
        this.group1 = group1;
    }
    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }
    public String getSelection() {
        return selection;
    }

    public void setSelection(String selection) {
        this.selection = selection;
    }
    public String getGrayed() {
        return grayed;
    }

    public void setGrayed(String grayed) {
        this.grayed = grayed;
    }


}