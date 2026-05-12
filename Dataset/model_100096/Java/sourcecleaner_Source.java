





import java.util.List;
import java.util.ArrayList;

public class sourcecleaner_Source extends LocatedElement {

    private String content;
    private boolean mark;
    private boolean handled;
    private String comment;



    public sourcecleaner_Source(
        String content,        boolean mark,        boolean handled,        String comment    ) {
        super(
        );
        this.content = content;
        this.mark = mark;
        this.handled = handled;
        this.comment = comment;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
    public boolean getMark() {
        return mark;
    }

    public void setMark(boolean mark) {
        this.mark = mark;
    }
    public boolean getHandled() {
        return handled;
    }

    public void setHandled(boolean handled) {
        this.handled = handled;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }


}