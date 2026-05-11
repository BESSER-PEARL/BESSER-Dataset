





import java.util.List;
import java.util.ArrayList;

public class website_ImageUnit extends DynamicUnit, CollectionUnit {

    private String missingImagePath;
    private int transitionTime;
    private int showTime;





    private website_ImageManipulation website_imagemanipulation;




    private website_Selection website_selection;


    public website_ImageUnit(
        String missingImagePath,        int transitionTime,        int showTime    ) {
        super(
        );
        this.missingImagePath = missingImagePath;
        this.transitionTime = transitionTime;
        this.showTime = showTime;
    }


    public String getMissingimagepath() {
        return missingImagePath;
    }

    public void setMissingimagepath(String missingImagePath) {
        this.missingImagePath = missingImagePath;
    }
    public int getTransitiontime() {
        return transitionTime;
    }

    public void setTransitiontime(int transitionTime) {
        this.transitionTime = transitionTime;
    }
    public int getShowtime() {
        return showTime;
    }

    public void setShowtime(int showTime) {
        this.showTime = showTime;
    }

    public website_ImageManipulation getWebsite_imagemanipulation() {
        return website_imagemanipulation;
    }

    public void setWebsite_imagemanipulation(website_ImageManipulation website_imagemanipulation) {
        this.website_imagemanipulation = website_imagemanipulation;
    }
    public website_Selection getWebsite_selection() {
        return website_selection;
    }

    public void setWebsite_selection(website_Selection website_selection) {
        this.website_selection = website_selection;
    }

}