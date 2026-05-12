





import java.util.List;
import java.util.ArrayList;

public class Document  {






    private List<image> images;


    public Document(
    ) {
        this.images = new ArrayList<>();
    }

    public Document(
        ArrayList<image> images    ) {
        this.images = images;
    }


    public List<image> getImages() {
        return images;
    }

    public void addImage(Image image) {
        this.images.add(image);
    }

}