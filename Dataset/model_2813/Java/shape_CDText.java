





import java.util.List;
import java.util.ArrayList;

public class shape_CDText extends ShapeConnection {

    private String texttype;





    private shape_TextBody shape_textbody;


    public shape_CDText(
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

}