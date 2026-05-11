





import java.util.List;
import java.util.ArrayList;

public class di_Comment extends Shape {






    private di_Diagram di_diagram;




    private List<di_CommentLink> di_commentlinks;




    private di_CommentLink di_commentlink;


    public di_Comment(
    ) {
        super(
        );
        this.di_commentlinks = new ArrayList<>();
    }

    public di_Comment(
        ArrayList<di_CommentLink> di_commentlinks    ) {
        this.di_commentlinks = di_commentlinks;
    }


    public di_Diagram getDi_diagram() {
        return di_diagram;
    }

    public void setDi_diagram(di_Diagram di_diagram) {
        this.di_diagram = di_diagram;
    }
    public List<di_CommentLink> getDi_commentlinks() {
        return di_commentlinks;
    }

    public void addDi_commentlink(Di_commentlink di_commentlink) {
        this.di_commentlinks.add(di_commentlink);
    }
    public di_CommentLink getDi_commentlink() {
        return di_commentlink;
    }

    public void setDi_commentlink(di_CommentLink di_commentlink) {
        this.di_commentlink = di_commentlink;
    }

}