





import java.util.List;
import java.util.ArrayList;

public class Java_Annotation  {

    private String type;
    private String sentenceText;



    public Java_Annotation(
        String type,        String sentenceText    ) {
        this.type = type;
        this.sentenceText = sentenceText;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getSentencetext() {
        return sentenceText;
    }

    public void setSentencetext(String sentenceText) {
        this.sentenceText = sentenceText;
    }


}