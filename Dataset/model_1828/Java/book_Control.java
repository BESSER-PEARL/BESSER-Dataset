





import java.util.List;
import java.util.ArrayList;

public class book_Control extends Node {

    private String image;
    private String sound;





    private book_Layer book_layer;


    public book_Control(
        String image,        String sound    ) {
        super(
        );
        this.image = image;
        this.sound = sound;
    }


    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }
    public String getSound() {
        return sound;
    }

    public void setSound(String sound) {
        this.sound = sound;
    }

    public book_Layer getBook_layer() {
        return book_layer;
    }

    public void setBook_layer(book_Layer book_layer) {
        this.book_layer = book_layer;
    }

}