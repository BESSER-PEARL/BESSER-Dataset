





import java.util.List;
import java.util.ArrayList;

public class softGalleryLanguage_PresentationSegments  {

    private String presentationSName;
    private String presentationCName;
    private String presentationAName;





    private softGalleryLanguage_PresentationContent softgallerylanguage_presentationcontent;


    public softGalleryLanguage_PresentationSegments(
        String presentationSName,        String presentationCName,        String presentationAName    ) {
        this.presentationSName = presentationSName;
        this.presentationCName = presentationCName;
        this.presentationAName = presentationAName;
    }


    public String getPresentationsname() {
        return presentationSName;
    }

    public void setPresentationsname(String presentationSName) {
        this.presentationSName = presentationSName;
    }
    public String getPresentationcname() {
        return presentationCName;
    }

    public void setPresentationcname(String presentationCName) {
        this.presentationCName = presentationCName;
    }
    public String getPresentationaname() {
        return presentationAName;
    }

    public void setPresentationaname(String presentationAName) {
        this.presentationAName = presentationAName;
    }

    public softGalleryLanguage_PresentationContent getSoftgallerylanguage_presentationcontent() {
        return softgallerylanguage_presentationcontent;
    }

    public void setSoftgallerylanguage_presentationcontent(softGalleryLanguage_PresentationContent softgallerylanguage_presentationcontent) {
        this.softgallerylanguage_presentationcontent = softgallerylanguage_presentationcontent;
    }

}