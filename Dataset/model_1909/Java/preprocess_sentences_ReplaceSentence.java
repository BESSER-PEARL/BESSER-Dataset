





import java.util.List;
import java.util.ArrayList;

public class preprocess_sentences_ReplaceSentence extends PreprocessingSentence {

    private boolean switch;



    public preprocess_sentences_ReplaceSentence(
        boolean switch    ) {
        super(
        );
        this.switch = switch;
    }


    public boolean getSwitch() {
        return switch;
    }

    public void setSwitch(boolean switch) {
        this.switch = switch;
    }


}