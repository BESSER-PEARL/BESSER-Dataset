





import java.util.List;
import java.util.ArrayList;

public class JavaSimplified_Comment extends StringElement {

    private boolean isJavadoc;



    public JavaSimplified_Comment(
        boolean isJavadoc    ) {
        super(
        );
        this.isJavadoc = isJavadoc;
    }


    public boolean getIsjavadoc() {
        return isJavadoc;
    }

    public void setIsjavadoc(boolean isJavadoc) {
        this.isJavadoc = isJavadoc;
    }


}