





import java.util.List;
import java.util.ArrayList;

public class presentation_Button extends Control {

    private String image;
    private String alignment;
    private String selection;
    private String group1;
    private String grayed;
    private String text;



    public presentation_Button(
        String image,        String alignment,        String selection,        String group1,        String grayed,        String text    ) {
        super(
        );
        this.image = image;
        this.alignment = alignment;
        this.selection = selection;
        this.group1 = group1;
        this.grayed = grayed;
        this.text = text;
    }


    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }
    public String getAlignment() {
        return alignment;
    }

    public void setAlignment(String alignment) {
        this.alignment = alignment;
    }
    public String getSelection() {
        return selection;
    }

    public void setSelection(String selection) {
        this.selection = selection;
    }
    public String getGroup1() {
        return group1;
    }

    public void setGroup1(String group1) {
        this.group1 = group1;
    }
    public String getGrayed() {
        return grayed;
    }

    public void setGrayed(String grayed) {
        this.grayed = grayed;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }


}