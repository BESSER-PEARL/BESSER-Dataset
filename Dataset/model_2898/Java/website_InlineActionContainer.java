





import java.util.List;
import java.util.ArrayList;

public class website_InlineActionContainer  {






    private website_InlineAction website_inlineaction;




    private List<website_InlineAction> website_inlineactions;


    public website_InlineActionContainer(
    ) {
        this.website_inlineactions = new ArrayList<>();
    }

    public website_InlineActionContainer(
        ArrayList<website_InlineAction> website_inlineactions    ) {
        this.website_inlineactions = website_inlineactions;
    }


    public website_InlineAction getWebsite_inlineaction() {
        return website_inlineaction;
    }

    public void setWebsite_inlineaction(website_InlineAction website_inlineaction) {
        this.website_inlineaction = website_inlineaction;
    }
    public List<website_InlineAction> getWebsite_inlineactions() {
        return website_inlineactions;
    }

    public void addWebsite_inlineaction(Website_inlineaction website_inlineaction) {
        this.website_inlineactions.add(website_inlineaction);
    }

}