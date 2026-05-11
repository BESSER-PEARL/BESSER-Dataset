





import java.util.List;
import java.util.ArrayList;

public class commons_CanonicalSluggable extends Sluggable {

    private String canonicalSlug;



    public commons_CanonicalSluggable(
        String canonicalSlug    ) {
        super(
        );
        this.canonicalSlug = canonicalSlug;
    }


    public String getCanonicalslug() {
        return canonicalSlug;
    }

    public void setCanonicalslug(String canonicalSlug) {
        this.canonicalSlug = canonicalSlug;
    }


}