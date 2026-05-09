





import java.util.List;
import java.util.ArrayList;

public class preprocess_sentences_CopySentence extends sentences_PreprocessingSentence, commons_LibraryElement, commons_NamedElement {

    private boolean suppress;



    public preprocess_sentences_CopySentence(
        boolean suppress    ) {
        super(
        );
        this.suppress = suppress;
    }


    public boolean getSuppress() {
        return suppress;
    }

    public void setSuppress(boolean suppress) {
        this.suppress = suppress;
    }


}