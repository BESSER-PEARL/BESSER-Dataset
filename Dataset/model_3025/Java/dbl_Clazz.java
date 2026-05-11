





import java.util.List;
import java.util.ArrayList;

public class dbl_Clazz extends LanguageConceptClassifier, Construct, ClassSimilar, Classifier {

    private boolean active;



    public dbl_Clazz(
        boolean active    ) {
        super(
        );
        this.active = active;
    }


    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }


}