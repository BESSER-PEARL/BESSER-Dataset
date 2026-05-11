





import java.util.List;
import java.util.ArrayList;

public class model_CurlyBrace extends SkinSupport, TextLinksSupport, AnnotationSupport, Widget, FontSupport, ColorForegroundSupport {

    private String position;



    public model_CurlyBrace(
        String position    ) {
        super(
        );
        this.position = position;
    }


    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }


}