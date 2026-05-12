





import java.util.List;
import java.util.ArrayList;

public class story_Persona extends User {

    private String picture;



    public story_Persona(
        String picture    ) {
        super(
        );
        this.picture = picture;
    }


    public String getPicture() {
        return picture;
    }

    public void setPicture(String picture) {
        this.picture = picture;
    }


}