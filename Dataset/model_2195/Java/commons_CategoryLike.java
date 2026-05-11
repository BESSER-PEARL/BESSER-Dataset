





import java.util.List;
import java.util.ArrayList;

public class commons_CategoryLike extends Positionable, NsPrefixable, Imageable, NameContainer, Sluggable, Identifiable {

    private String slugPath;
    private String categoryCount;
    private String imageId;
    private String level;
    private String color;



    public commons_CategoryLike(
        String slugPath,        String categoryCount,        String imageId,        String level,        String color    ) {
        super(
        );
        this.slugPath = slugPath;
        this.categoryCount = categoryCount;
        this.imageId = imageId;
        this.level = level;
        this.color = color;
    }


    public String getSlugpath() {
        return slugPath;
    }

    public void setSlugpath(String slugPath) {
        this.slugPath = slugPath;
    }
    public String getCategorycount() {
        return categoryCount;
    }

    public void setCategorycount(String categoryCount) {
        this.categoryCount = categoryCount;
    }
    public String getImageid() {
        return imageId;
    }

    public void setImageid(String imageId) {
        this.imageId = imageId;
    }
    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }


}