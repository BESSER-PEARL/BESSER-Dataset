





import java.util.List;
import java.util.ArrayList;

public class website_ImageManipulation extends NamedElement {

    private int jpegQuality;





    private website_WebGenModel website_webgenmodel;


    public website_ImageManipulation(
        int jpegQuality    ) {
        super(
        );
        this.jpegQuality = jpegQuality;
    }


    public int getJpegquality() {
        return jpegQuality;
    }

    public void setJpegquality(int jpegQuality) {
        this.jpegQuality = jpegQuality;
    }

    public website_WebGenModel getWebsite_webgenmodel() {
        return website_webgenmodel;
    }

    public void setWebsite_webgenmodel(website_WebGenModel website_webgenmodel) {
        this.website_webgenmodel = website_webgenmodel;
    }

}