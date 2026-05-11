





import java.util.List;
import java.util.ArrayList;

public class mprologTermReference_Functor extends Term {

    private String text;





    private mprologTermReference_Head mprologtermreference_head;


    public mprologTermReference_Functor(
        String text    ) {
        super(
        );
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public mprologTermReference_Head getMprologtermreference_head() {
        return mprologtermreference_head;
    }

    public void setMprologtermreference_head(mprologTermReference_Head mprologtermreference_head) {
        this.mprologtermreference_head = mprologtermreference_head;
    }

}