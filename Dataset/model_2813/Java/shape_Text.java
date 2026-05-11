





import java.util.List;
import java.util.ArrayList;

public class shape_Text extends Shape {

    private String texttype;





    private shape_TextBody shape_textbody;




    private shape_TextLayout shape_textlayout;


    public shape_Text(
        String texttype    ) {
        super(
        );
        this.texttype = texttype;
    }


    public String getTexttype() {
        return texttype;
    }

    public void setTexttype(String texttype) {
        this.texttype = texttype;
    }

    public shape_TextBody getShape_textbody() {
        return shape_textbody;
    }

    public void setShape_textbody(shape_TextBody shape_textbody) {
        this.shape_textbody = shape_textbody;
    }
    public shape_TextLayout getShape_textlayout() {
        return shape_textlayout;
    }

    public void setShape_textlayout(shape_TextLayout shape_textlayout) {
        this.shape_textlayout = shape_textlayout;
    }

}