





import java.util.List;
import java.util.ArrayList;

public class sample_Annotation  {

    private String Type;
    private String Text;





    private sample_Sentence sample_sentence;


    public sample_Annotation(
        String Type,        String Text    ) {
        this.Type = Type;
        this.Text = Text;
    }


    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }
    public String getText() {
        return Text;
    }

    public void setText(String Text) {
        this.Text = Text;
    }

    public sample_Sentence getSample_sentence() {
        return sample_sentence;
    }

    public void setSample_sentence(sample_Sentence sample_sentence) {
        this.sample_sentence = sample_sentence;
    }

}