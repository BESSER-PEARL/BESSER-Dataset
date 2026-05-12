





import java.util.List;
import java.util.ArrayList;

public class Vote  {

    private boolean tipo;





    private Comment comment;




    private Post post;


    public Vote(
        boolean tipo    ) {
        this.tipo = tipo;
    }


    public boolean getTipo() {
        return tipo;
    }

    public void setTipo(boolean tipo) {
        this.tipo = tipo;
    }

    public Comment getComment() {
        return comment;
    }

    public void setComment(Comment comment) {
        this.comment = comment;
    }
    public Post getPost() {
        return post;
    }

    public void setPost(Post post) {
        this.post = post;
    }

}