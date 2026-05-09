





import java.util.List;
import java.util.ArrayList;

public class express_algorithms_Statement  {

    private String text;





    private RepeatStatement repeatstatement;




    private Algorithm algorithm;


    public express_algorithms_Statement(
        String text    ) {
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public RepeatStatement getRepeatstatement() {
        return repeatstatement;
    }

    public void setRepeatstatement(RepeatStatement repeatstatement) {
        this.repeatstatement = repeatstatement;
    }
    public Algorithm getAlgorithm() {
        return algorithm;
    }

    public void setAlgorithm(Algorithm algorithm) {
        this.algorithm = algorithm;
    }

}